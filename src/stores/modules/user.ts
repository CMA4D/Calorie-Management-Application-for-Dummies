import { defineStore } from 'pinia'

interface UserInfo {
  id: string
  username: string
  nickname: string
  avatar: string
  email: string
}

interface UserState {
  userInfo: UserInfo | null
  token: string | null
  rememberPassword: boolean
}

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    userInfo: null,
    token: null,
    rememberPassword: false
  }),
  
  getters: {
    isLoggedIn: (state) => !!state.token
  },
  
  actions: {
    // 登录
    async login(username: string, password: string, remember: boolean) {
      try {
        // TODO: 替换为实际的登录 API
        // const response = await uni.request({
        //   url: 'YOUR_API_URL/login',
        //   method: 'POST',
        //   data: { username, password }
        // })
        
        // 模拟登录成功
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        // 保存用户信息
        this.userInfo = {
          id: '1',
          username,
          nickname: '测试用户',
          avatar: '/static/logo.png',
          email: 'test@example.com'
        }
        
        // 保存 token
        this.token = 'mock_token'
        
        // 保存记住密码状态
        this.rememberPassword = remember
        
        // 保存到本地存储
        if (remember) {
          uni.setStorageSync('username', username)
          uni.setStorageSync('password', password)
        } else {
          uni.removeStorageSync('username')
          uni.removeStorageSync('password')
        }
        
        return true
      } catch (error) {
        console.error('登录失败：', error)
        return false
      }
    },
    
    // 注册
    async register(data: { username: string; password: string; email: string }) {
      try {
        // TODO: 替换为实际的注册 API
        // const response = await uni.request({
        //   url: 'YOUR_API_URL/register',
        //   method: 'POST',
        //   data
        // })
        
        // 模拟注册成功
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        return true
      } catch (error) {
        console.error('注册失败：', error)
        return false
      }
    },
    
    // 重置密码
    async resetPassword(email: string) {
      try {
        // TODO: 替换为实际的重置密码 API
        // const response = await uni.request({
        //   url: 'YOUR_API_URL/reset-password',
        //   method: 'POST',
        //   data: { email }
        // })
        
        // 模拟发送重置密码邮件
        await new Promise(resolve => setTimeout(resolve, 1000))
        
        return true
      } catch (error) {
        console.error('重置密码失败：', error)
        return false
      }
    },
    
    // 退出登录
    logout() {
      this.userInfo = null
      this.token = null
      this.rememberPassword = false
      
      // 清除本地存储
      uni.removeStorageSync('token')
      uni.removeStorageSync('userInfo')
    },
    
    // 检查登录状态
    checkLoginStatus() {
      const token = uni.getStorageSync('token')
      const userInfo = uni.getStorageSync('userInfo')
      
      if (token && userInfo) {
        this.token = token
        this.userInfo = userInfo
        return true
      }
      
      return false
    }
  }
}) 