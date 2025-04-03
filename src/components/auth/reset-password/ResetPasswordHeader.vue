<template>
  <view class="reset-password-header">
    <text class="title">重置密码</text>
    <text class="subtitle">请输入您的账号和验证码</text>
  </view>
</template>

<script setup lang="ts">
defineOptions({
  name: 'ResetPasswordHeader'
})
</script>

<style lang="scss">
.reset-password-header {
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