<template>
  <view class="home-header">
    <text class="title">卡路里监测</text>
    <view class="user-info">
      <text class="nickname">{{ nickname }}</text>
      <image class="avatar" :src="avatar" mode="aspectFill" />
    </view>
  </view>
</template>

<script setup lang="ts">
// 定义组件名称
defineOptions({
  name: 'homeHeader'
})

// 定义组件属性
interface Props {
  nickname: string
  avatar: string
}

defineProps<Props>()
</script>

<style lang="scss">
/* 首页头部样式 */
.home-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  
  /* 标题样式 */
  .title {
    font-size: 24px;
    font-weight: bold;
    color: #333;
  }
  
  /* 用户信息样式 */
  .user-info {
    display: flex;
    align-items: center;
    
    /* 昵称样式 */
    .nickname {
      font-size: 16px;
      color: #666;
      margin-right: 10px;
    }
    
    /* 头像样式 */
    .avatar {
      width: 40px;
      height: 40px;
      border-radius: 20px;
    }
  }
}
</style> 