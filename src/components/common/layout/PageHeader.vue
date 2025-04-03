<template>
  <view class="page-header">
    <view class="back-button" @click="handleBack">
      <text class="iconfont icon-back">←</text>
    </view>
    <text class="title">{{ title }}</text>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'pageHeader'
})

// 定义属性
const props = defineProps<{
  title: string
}>()

// 处理返回
const handleBack = () => {
  uni.navigateBack()
}
</script>

<style lang="scss">
/* 页面头部样式 */
.page-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  
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