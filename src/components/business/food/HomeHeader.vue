<template>
  <view class="home-header">
    <view class="user-info">
      <image class="avatar" :src="avatar" mode="aspectFill" />
      <text class="nickname">{{ nickname }}</text>
    </view>
  </view>
</template>

<script setup lang="ts">
defineProps<{
  nickname: string
  avatar: string
}>()

defineOptions({
  name: 'HomeHeader'
})
</script>

<style lang="scss">
.home-header {
  background-color: #fff;
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);

  .user-info {
    display: flex;
    align-items: center;
    gap: 12px;

    .avatar {
      width: 48px;
      height: 48px;
      border-radius: 24px;
    }

    .nickname {
      font-size: 18px;
      font-weight: 500;
      color: #333;
    }
  }
}
</style> 