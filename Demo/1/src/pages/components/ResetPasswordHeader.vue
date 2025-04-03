<template>
  <view class="reset-password-header">
    <!-- 返回按钮 -->
    <view class="back-button" @click="handleBack">
      <text class="iconfont icon-back">←</text>
    </view>
    
    <!-- 标题 -->
    <text class="title">找回密码</text>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'resetPasswordHeader'
})

// 处理返回按钮点击
const handleBack = () => {
  uni.navigateBack()
}
</script>

<style lang="scss">
/* 找回密码头部样式 */
.reset-password-header {
  display: flex;
  align-items: center;
  margin-bottom: 30px;
  
  /* 返回按钮样式 */
  .back-button {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 10px;
    
    .icon-back {
      font-size: 24px;
      color: #333;
    }
  }
  
  /* 标题样式 */
  .title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
  }
}
</style> 