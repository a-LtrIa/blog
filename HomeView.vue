<template>
  <div class="home-container">
    <!-- 页面标题 -->
    <header class="page-header">
      <h1>我的博客</h1>
      <p>记录技术与生活</p>
    </header>

    <!-- 主内容区：Flex 布局 -->
    <main class="content-wrapper">
      <!-- 个人简介卡片 -->
      <section class="card intro-card">
        <h2 class="card-title">关于我</h2>
        <div class="card-body">
          <img src="@/assets/avatar.png" alt="我的头像" class="avatar" />
          <p>你好，我是 <strong>张三</strong>，一名热爱编程与写作的开发者。</p>
          <p>主要技术栈：Python、Django、Vue.js、Linux。</p>
          <p>在这里，我分享技术笔记、学习心得与生活感悟。</p>
          <div class="social-links">
            <a href="https://github.com/yourname" target="_blank">GitHub</a> |
            <a href="mailto:you@example.com">邮箱</a>
          </div>
        </div>
      </section>

      <!-- 网站简介卡片 -->
      <section class="card site-card">
        <h2 class="card-title">关于本站</h2>
        <div class="card-body">
          <p>这是一个由 <strong>Django + Vue</strong> 驱动的个人博客。</p>
          <p>✅ 内容专注：技术分享、学习笔记、项目实践</p>
          <p>✅ 极简设计：无广告、无追踪、专注阅读体验</p>
          <p>✅ 持续更新：每周至少一篇原创文章</p>
          <p>所有内容均为原创或深度整理，欢迎留言交流。</p>
        </div>
      </section>

      <!-- ✅ 新增：文章列表卡片 -->
      <section class="card posts-card">
        <h2 class="card-title">最新文章</h2>
        <div class="card-body">
          <!-- 加载状态 -->
          <div v-if="loading" class="loading">
            <p>加载中...</p>
          </div>

          <!-- 错误状态 -->
          <div v-else-if="error" class="error">
            <p>加载文章失败：{{ error }}</p>
          </div>

          <!-- 文章列表 -->
          <ul v-else class="posts-list">
            <li v-for="post in posts" :key="post.id" class="post-item">
              <router-link :to="`/post/${post.id}`" class="post-link">
                <h3 class="post-title">{{ post.title }}</h3>
                <p class="post-excerpt">{{ truncate(post.content, 80) }}</p>
                <time class="post-date">{{ formatDate(post.created_at) }}</time>
              </router-link>
            </li>
          </ul>

          <!-- 无文章提示 -->
          <p v-if="!loading && !error && posts.length === 0">
            暂无文章发布。
          </p>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 响应式数据
const posts = ref([])
const loading = ref(true)
const error = ref(null)

// 获取文章列表
const fetchPosts = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/posts/')
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    posts.value = await response.json()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

// 页面加载时获取数据
onMounted(() => {
  fetchPosts()
})

// 工具函数：截取文本
const truncate = (text, length) => {
  if (!text) return ''
  return text.length > length ? text.slice(0, length) + '...' : text
}

// 格式化日期
const formatDate = (isoDate) => {
  const date = new Date(isoDate)
  return date.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>

<style scoped>
.home-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 20px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  color: #333;
  line-height: 1.8;
}

.page-header {
  text-align: center;
  margin-bottom: 40px;
}

.page-header h1 {
  font-size: 2.5em;
  margin: 0;
  color: #1a1a1a;
}

.page-header p {
  margin: 10px 0 0;
  color: #666;
  font-size: 1.1em;
}

/* 主内容区：Flex 布局 */
.content-wrapper {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
}

.card {
  flex: 1 1 400px;
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.card-title {
  margin: 0;
  padding: 20px 24px 16px;
  font-size: 1.5em;
  color: #2c3e50;
  border-bottom: 1px solid #eee;
}

.card-body {
  padding: 24px;
  font-size: 1em;
  color: #444;
}

/* 个人简介卡片样式 */
.intro-card .avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 16px;
  border: 3px solid #eee;
}

.intro-card p {
  margin: 12px 0;
}

.social-links {
  margin-top: 16px;
  font-size: 0.95em;
}

.social-links a {
  color: #42b983;
  text-decoration: none;
}

.social-links a:hover {
  text-decoration: underline;
}

/* ✅ 文章列表样式 */
.posts-card {
  flex: 2 1 600px; /* 宽一些，占更多空间 */
}

.posts-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.post-item {
  border-bottom: 1px dashed #eee;
  padding: 16px 0;
}

.post-item:first-child {
  padding-top: 0;
}

.post-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.post-link {
  text-decoration: none;
  color: inherit;
  display: block;
  transition: color 0.2s;
}

.post-link:hover {
  color: #42b983;
}

.post-title {
  margin: 0 0 8px;
  font-size: 1.3em;
  color: #2c3e50;
}

.post-excerpt {
  margin: 0;
  color: #666;
  font-size: 0.95em;
  line-height: 1.6;
}

.post-date {
  display: block;
  margin-top: 8px;
  font-size: 0.85em;
  color: #999;
  font-style: italic;
}

.loading, .error {
  text-align: center;
  color: #999;
  font-style: italic;
}

.error {
  color: #e74c3c;
}

/* 响应式：小屏幕下堆叠显示 */
@media (max-width: 768px) {
  .content-wrapper {
    flex-direction: column;
  }

  .page-header h1 {
    font-size: 2em;
  }

  .home-container {
    padding: 20px;
  }

  .posts-card {
    flex: 1 1 100%;
  }
}
</style>