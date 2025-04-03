// 食物数据接口
export interface FoodData {
  image: string
  weight: number
  foods: string[]
  dishes: string[]
  calories: number
  timestamp: string
}

// 卡路里数据接口
export interface CalorieData {
  foods: string[]
  dishes: string[]
  calories: number
  advice: string
}

// 扫描结果接口
export interface ScanResult {
  image: string
  weight: number
  calorieData: CalorieData
} 