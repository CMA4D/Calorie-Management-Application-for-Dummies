<template>
  <view class="login-header">
    <image class="logo" src="/static/logo.png" mode="aspectFit" />
    <text class="title">食物卡路里识别</text>
    <text class="subtitle">智能识别食物，轻松管理卡路里</text>
  </view>
</template>

<script setup lang="ts">
defineOptions({
  name: 'LoginHeader'
})
</script>

<style lang="scss">
.login-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 0;
  
  .logo {
    width: 80px;
    height: 80px;
    margin-bottom: 20px;
  }
  
  .title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 10px;
  }
  
  .subtitle {
    font-size: 14px;
    color: #666;
  }
}
</style> 