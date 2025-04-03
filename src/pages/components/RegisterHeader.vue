<template>
  <view class="register-header">
    <!-- 返回按钮 -->
    <view class="back-button" @click="handleBack">
      <text class="iconfont">←</text>
    </view>
    
    <!-- 页面标题 -->
    <text class="title">用户注册</text>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'registerHeader'
})

// 处理返回按钮点击
const handleBack = () => {
  uni.navigateBack()
}
</script>

<style lang="scss">
/* 注册头部样式 */
.register-header {
  position: relative;
  margin-top: 40px;
  margin-bottom: 40px;
  text-align: center;
  
  /* 返回按钮样式 */
  .back-button {
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    
    .iconfont {
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