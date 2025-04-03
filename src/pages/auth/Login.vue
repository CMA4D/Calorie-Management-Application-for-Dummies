<template>
  <view class="login-container">
    <!-- 登录页面头部 -->
    <LoginHeader />
    
    <!-- 登录表单 -->
    <LoginForm 
      :loading="loading"
      @submit="handleLogin"
    />
    
    <!-- 登录页面底部 -->
    <LoginFooter />

    <!-- 调试按钮组 -->
    <view class="debug-buttons" v-if="isDevelopment">
      <button @click="simulateLoginSuccess">模拟登录成功</button>
      <button @click="simulateUserNotExist">模拟用户不存在</button>
      <button @click="simulatePasswordError">模拟密码错误</button>
    </view>
  </view>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/modules/user'
import LoginHeader from '@/components/auth/login/LoginHeader.vue'
import LoginForm from '@/components/auth/login/LoginForm.vue'
import LoginFooter from '@/components/auth/login/LoginFooter.vue'

// 定义组件名称
defineOptions({
  name: 'Login'
})

// 登录加载状态
const loading = ref(false)

// 是否为开发环境
const isDevelopment = process.env.NODE_ENV === 'development'

// 用户状态管理
const userStore = useUserStore()

// 登录表单引用
const loginFormRef = ref<InstanceType<typeof LoginForm> | null>(null)

// 处理登录逻辑
const handleLogin = async (data: { username: string; password: string; remember: boolean }) => {
  try {
    loading.value = true
    
    // 登录
    const success = await userStore.login(data.username, data.password, data.remember)
    
    if (success) {
      // 如果选择记住密码，保存到本地存储
      if (data.remember) {
        uni.setStorageSync('rememberedUsername', data.username)
        uni.setStorageSync('rememberedPassword', data.password)
      } else {
        // 如果未选择记住密码，清除本地存储
        uni.removeStorageSync('rememberedUsername')
        uni.removeStorageSync('rememberedPassword')
      }
      
      uni.showToast({
        title: '登录成功',
        icon: 'success'
      })
      
      // 延迟跳转
      setTimeout(() => {
        uni.reLaunch({
          url: '/pages/home/Home'
        })
      }, 1500)
    } else {
      uni.showToast({
        title: '用户名或密码错误',
        icon: 'none'
      })
    }
  } catch (error) {
    console.error('登录失败：', error)
    uni.showToast({
      title: '登录失败，请重试',
      icon: 'error'
    })
  } finally {
    loading.value = false
  }
}

// 页面加载时检查是否有记住的账号密码
onMounted(() => {
  const rememberedUsername = uni.getStorageSync('rememberedUsername')
  const rememberedPassword = uni.getStorageSync('rememberedPassword')
  
  if (rememberedUsername && rememberedPassword) {
    // 触发登录表单的记住密码
    loginFormRef.value?.setRememberedCredentials(rememberedUsername, rememberedPassword)
  }
})

// 模拟登录成功
const simulateLoginSuccess = async () => {
  loading.value = true
  await new Promise(resolve => setTimeout(resolve, 1000))
  uni.showToast({
    title: '登录成功',
    icon: 'success'
  })
  setTimeout(() => {
    uni.reLaunch({
      url: '/pages/home/Home'
    })
  }, 1500)
  loading.value = false
}

// 模拟用户不存在
const simulateUserNotExist = () => {
  uni.showModal({
    title: '提示',
    content: '用户名错误，该用户不存在',
    showCancel: false,
    success: () => {
      // 可以选择跳转到注册页面
      uni.navigateTo({
        url: '/pages/auth/Register'
      })
    }
  })
}

// 模拟密码错误
const simulatePasswordError = () => {
  uni.showModal({
    title: '提示',
    content: '用户名或密码错误',
    confirmText: '找回密码',
    cancelText: '重试',
    success: (res) => {
      if (res.confirm) {
        uni.navigateTo({
          url: '/pages/auth/ResetPassword'
        })
      }
    }
  })
}
</script>

<style lang="scss">
/* 登录页面容器样式 */
.login-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #f5f5f5;
  padding: 20px;
}

/* 调试按钮组样式 */
.debug-buttons {
  margin-top: 20px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  
  button {
    margin-bottom: 10px;
    background-color: #f0f0f0;
    color: #666;
    
    &:last-child {
      margin-bottom: 0;
    }
  }
}
</style> 