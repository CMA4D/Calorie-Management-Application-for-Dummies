<template>
  <view class="reset-password-footer">
    <text class="copyright">© 2024 卡路里监测系统</text>
    <text class="version">Version 1.0.0</text>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'resetPasswordFooter'
})
</script>

<style lang="scss">
/* 找回密码页脚样式 */
.reset-password-footer {
  margin-top: 40px;
  padding: 20px;
  text-align: center;
  
  /* 版权信息样式 */
  .copyright {
    font-size: 12px;
    color: #999;
    display: block;
    margin-bottom: 8px;
  }
  
  /* 版本信息样式 */
  .version {
    font-size: 12px;
    color: #999;
  }
}
</style> 