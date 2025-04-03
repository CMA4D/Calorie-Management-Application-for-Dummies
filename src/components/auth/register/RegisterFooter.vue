<template>
  <view class="register-footer">
    <text class="text">已有账号？</text>
    <text class="link" @click="goToLogin">立即登录</text>
  </view>
</template>

<script setup lang="ts">
defineOptions({
  name: 'RegisterFooter'
})

// 跳转到登录页面
const goToLogin = () => {
  uni.navigateBack()
}
</script>

<style lang="scss">
.register-footer {
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