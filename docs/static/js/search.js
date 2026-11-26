// 静态博客本地搜索功能
// 无需后端，纯前端JS实现本地搜索
document.addEventListener('DOMContentLoaded', function() {
  // 搜索输入框快捷键支持
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    // Ctrl/Cmd + K 聚焦搜索框
    document.addEventListener('keydown', function(e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        searchInput.focus();
      }
      // ESC 失焦
      if (e.key === 'Escape' && document.activeElement === searchInput) {
        searchInput.blur();
      }
    });
  }
});