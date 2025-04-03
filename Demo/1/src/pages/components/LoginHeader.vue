<template>
  <view class="login-header">
    <!-- 应用标题 -->
    <text class="title">卡路里监测系统</text>
    <!-- 欢迎文本 -->
    <text class="welcome">欢迎使用</text>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'loginHeader'
})
</script>

<style lang="scss">
/* 登录头部样式 */
.login-header {
  margin-top: 60px;
  margin-bottom: 40px;
  text-align: center;
  
  /* 标题样式 */
  .title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    display: block;
    margin-bottom: 10px;
  }
  
  /* 欢迎文本样式 */
  .welcome {
    font-size: 16px;
    color: #666;
  }
}
</style> 