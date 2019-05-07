package main

import (
  "fmt"
  "net/http"
  "../utils"
  "net/url"
  "strconv"
  //"os"
  "time"
)

//监控宝回调url处理
func jkbCallback(w http.ResponseWriter, r *http.Request) {

}




func handleCallback() {

}

func handleCallbackOld(post_data url.Values) {


}


//更改ums当前告警到历史告警
func fixCurrentWarn() {

}


//主函数
func main() {
  http.HandleFunc("/", jkbCallback)
  http.ListenAndServe(":8088", nil)
}





