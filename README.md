2027年后北邮信通院学生可依此参考
在此之前所有盗用追责到底


# 食物卡路里识别系统

基于 uni-app + Vue3 + TypeScript 开发的跨平台应用，用于识别食物并计算卡路里。

## 项目结构

```
src/
├── components/          # 组件目录
│   ├── common/         # 通用组件
│   │   ├── layout/     # 布局组件
│   │   ├── feedback/   # 反馈组件
│   │   └── data/       # 数据展示组件
│   └── business/       # 业务组件
│       ├── food/       # 食物相关组件
│       └── history/    # 历史记录相关组件
├── pages/              # 页面目录
│   ├── auth/          # 认证相关页面
│   ├── home/          # 首页相关页面
│   └── history/       # 历史记录相关页面
├── stores/            # 状态管理
│   └── modules/       # 状态模块
├── hooks/             # 组合式函数
├── types/             # 类型定义
├── utils/             # 工具函数
├── styles/            # 样式文件
└── static/            # 静态资源
```

## 开发环境

- Node.js >= 16
- Vue 3
- TypeScript
- uni-app
- Vite

## 安装依赖

```bash
npm install
```

## 开发

```bash
npm run dev:h5
npm run dev:mp-weixin
```

## 构建

```bash
npm run build:h5
npm run build:mp-weixin
```

## 技术栈

- Vue 3 - 渐进式 JavaScript 框架
- TypeScript - JavaScript 的超集
- uni-app - 使用 Vue.js 开发跨平台应用的前端框架
- Vite - 下一代前端构建工具
- Pinia - Vue 的状态管理库

## 开发规范

1. 组件命名：使用 PascalCase
2. 文件命名：使用 kebab-case
3. 变量命名：使用 camelCase
4. 常量命名：使用 UPPER_CASE
5. 类型定义：使用 PascalCase，以 Type 结尾

## 提交规范

- feat: 新功能
- fix: 修复问题
- docs: 文档修改
- style: 代码格式修改
- refactor: 代码重构
- test: 测试用例修改
- chore: 其他修改

## 许可证

Apache 2.0 License
