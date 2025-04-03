<template>
  <view class="reset-password-footer">
    <text class="text">想起密码了？</text>
    <text class="link" @click="goToLogin">立即登录</text>
  </view>
</template>

<script setup lang="ts">
defineOptions({
  name: 'ResetPasswordFooter'
})

// 跳转到登录页面
const goToLogin = () => {
  uni.navigateBack()
}
</script>

<style lang="scss">
.reset-password-footer {
  margin-top: 20px;
  text-align: center;
  
  .text {
    color: #666;
    font-size: 14px;
  }
  
  .link {
    color: #007AFF;
    font-size: 14px;
    margin-left: 5px;
  }
}
</style> 