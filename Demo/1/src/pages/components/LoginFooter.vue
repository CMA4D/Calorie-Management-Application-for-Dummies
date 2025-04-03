<template>
  <view class="login-footer">
    <!-- 版权信息 -->
    <text class="copyright">© 2025 卡路里监测系统</text>
    <!-- 版本信息 -->
    <text class="version">Version 1.0.0</text>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'loginFooter'
})
</script>

<style lang="scss">
/* 登录底部样式 */
.login-footer {
  margin-top: auto;
  padding: 20px 0;
  text-align: center;
  
  /* 版权信息样式 */
  .copyright {
    font-size: 12px;
    color: #999;
    display: block;
    margin-bottom: 4px;
  }
  
  /* 版本信息样式 */
  .version {
    font-size: 12px;
    color: #999;
  }
}
</style> 