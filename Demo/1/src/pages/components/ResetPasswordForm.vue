<template>
  <view class="reset-password-form">
    <!-- 说明文字 -->
    <view class="description">
      <text>请输入您注册时使用的邮箱，我们将向该邮箱发送新的密码。</text>
    </view>
    
    <!-- 邮箱输入框 -->
    <view class="form-item">
      <text class="label">邮箱</text>
      <input 
        type="text"
        v-model="formData.email"
        placeholder="请输入邮箱"
        :disabled="loading"
      />
    </view>
    
    <!-- 提交按钮 -->
    <button 
      class="submit-button"
      :loading="loading"
      :disabled="!isFormValid"
      @click="handleSubmit"
    >
      发送新密码
    </button>
  </view>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

// 定义组件名称
defineOptions({
  name: 'resetPasswordForm'
})

// 定义组件属性
interface Props {
  loading?: boolean
}

// 定义组件事件
interface Emits {
  (e: 'submit', data: { email: string }): void
}

const props = withDefaults(defineProps<Props>(), {
  loading: false
})

const emit = defineEmits<Emits>()

// 表单数据
const formData = ref({
  email: ''
})

// 表单验证
const isFormValid = computed(() => {
  const { email } = formData.value
  
  // 邮箱格式验证
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(email)
})

// 处理表单提交
const handleSubmit = () => {
  if (!isFormValid.value) return
  
  emit('submit', {
    email: formData.value.email.trim()
  })
}
</script>

<style lang="scss">
/* 找回密码表单样式 */
.reset-password-form {
  background-color: #fff;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  
  /* 说明文字样式 */
  .description {
    margin-bottom: 20px;
    color: #666;
    font-size: 14px;
    line-height: 1.5;
  }
  
  /* 表单项样式 */
  .form-item {
    margin-bottom: 20px;
    
    /* 标签样式 */
    .label {
      font-size: 14px;
      color: #333;
      margin-bottom: 8px;
      display: block;
    }
    
    /* 输入框样式 */
    input {
      width: 100%;
      height: 44px;
      border: 1px solid #ddd;
      border-radius: 4px;
      padding: 0 12px;
      font-size: 14px;
      
      &:focus {
        border-color: #007AFF;
      }
      
      &:disabled {
        background-color: #f5f5f5;
      }
    }
  }
  
  /* 提交按钮样式 */
  .submit-button {
    width: 100%;
    height: 44px;
    background-color: #007AFF;
    color: #fff;
    border-radius: 4px;
    font-size: 16px;
    margin-top: 30px;
    
    &:disabled {
      background-color: #ccc;
    }
  }
}
</style> 