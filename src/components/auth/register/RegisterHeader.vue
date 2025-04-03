<template>
  <view class="register-header">
    <text class="title">注册账号</text>
    <text class="subtitle">欢迎加入食物卡路里识别系统</text>
  </view>
</template>

<script setup lang="ts">
defineOptions({
  name: 'RegisterHeader'
})
</script>

<style lang="scss">
.register-header {
  padding: 40px 0;
  text-align: center;
  
  .title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 8px;
  }
  
  .subtitle {
    font-size: 14px;
    color: #666;
  }
}
</style> 