<template>
  <view class="register-footer">
    <text class="copyright">© 2024 卡路里监测系统</text>
    <text class="version">Version 1.0.0</text>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'registerFooter'
})
</script>

<style lang="scss">
/* 注册页脚样式 */
.register-footer {
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