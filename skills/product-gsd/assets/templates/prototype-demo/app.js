const state = {
  loading: false,
  selectedStatus: "all",
  records: []
};

async function loadData() {
  state.loading = true;
  render();
  const [sample, copy, spec] = await Promise.all([
    fetch("./data/sample-data.json").then((res) => res.json()),
    fetch("./data/copy.zh-CN.json").then((res) => res.json()),
    fetch("./spec/product-spec.json").then((res) => res.json())
  ]);
  state.records = sample.records;
  state.copy = copy;
  state.spec = spec;
  state.loading = false;
  render();
}

function filteredRecords() {
  if (state.selectedStatus === "all") return state.records;
  return state.records.filter((item) => item.status === state.selectedStatus);
}

function render() {
  const app = document.querySelector("#app");
  const copy = state.copy || { title: "Prototype Demo", subtitle: "加载中" };
  const rows = filteredRecords();
  app.innerHTML = `
    <div class="shell" data-pm-id="demo.shell">
      <aside class="sidebar" data-pm-id="demo.sidebar">
        <h1>${copy.title}</h1>
        <p>${copy.subtitle}</p>
      </aside>
      <main class="main" data-pm-id="demo.main">
        <section class="card" data-pm-id="demo.list-card">
          <h2>${copy.listTitle || "记录列表"}</h2>
          <div class="toolbar" data-pm-id="demo.toolbar">
            <select data-pm-id="demo.filter.status" aria-label="状态筛选">
              <option value="all">全部状态</option>
              <option value="active">生效中</option>
              <option value="draft">草稿</option>
              <option value="paused">已停用</option>
            </select>
            <button class="primary" data-pm-id="demo.action.primary">${copy.primaryAction || "创建策略"}</button>
            <button data-pm-id="demo.action.simulate-error">${copy.errorAction || "模拟异常"}</button>
          </div>
          ${state.loading ? `<div class="state" data-pm-id="demo.state.loading">加载中...</div>` : renderTable(rows)}
          <div class="state" data-pm-id="demo.state.feedback">${copy.feedback || "选择筛选条件或点击操作按钮查看反馈。"}</div>
        </section>
      </main>
    </div>
  `;
  bindEvents();
}

function renderTable(rows) {
  if (!rows.length) {
    return `<div class="state" data-pm-id="demo.state.empty">暂无符合条件的数据。</div>`;
  }
  return `
    <table data-pm-id="demo.table">
      <thead>
        <tr>
          <th>名称</th>
          <th>状态</th>
          <th>负责人</th>
          <th>风险</th>
          <th>更新时间</th>
        </tr>
      </thead>
      <tbody>
        ${rows.map((item) => `
          <tr data-pm-id="demo.table.row.${item.id}">
            <td>${item.name}</td>
            <td><span class="badge">${item.statusLabel}</span></td>
            <td>${item.owner}</td>
            <td>${item.risk}</td>
            <td>${item.updatedAt}</td>
          </tr>
        `).join("")}
      </tbody>
    </table>
  `;
}

function bindEvents() {
  const filter = document.querySelector('[data-pm-id="demo.filter.status"]');
  if (filter) {
    filter.value = state.selectedStatus;
    filter.addEventListener("change", (event) => {
      state.selectedStatus = event.target.value;
      render();
    });
  }

  document.querySelector('[data-pm-id="demo.action.primary"]')?.addEventListener("click", () => {
    document.querySelector('[data-pm-id="demo.state.feedback"]').textContent = "已创建一条 mock 策略，生产接入时需替换为真实保存接口。";
  });

  document.querySelector('[data-pm-id="demo.action.simulate-error"]')?.addEventListener("click", () => {
    document.querySelector('[data-pm-id="demo.state.feedback"]').textContent = "模拟异常：当前供应侧数据不可用，请检查重试策略。";
  });
}

loadData();

