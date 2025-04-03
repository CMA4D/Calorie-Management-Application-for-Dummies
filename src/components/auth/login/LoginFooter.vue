<template>
  <view class="login-footer">
    <text class="copyright">© 2024 食物卡路里识别</text>
    <text class="version">Version 1.0.0</text>
  </view>
</template>

<script setup lang="ts">
defineOptions({
  name: 'LoginFooter'
})
</script>

<style lang="scss">
.login-footer {
  margin-top: auto;
  padding: 20px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  
  .copyright {
    font-size: 12px;
    color: #999;
    margin-bottom: 5px;
  }
  
  .version {
    font-size: 12px;
    color: #999;
  }
}
</style> 