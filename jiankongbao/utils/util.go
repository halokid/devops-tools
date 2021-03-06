package utils

import (
  "os"
  "fmt"
  "crypto/md5"
)


//md5加密
func SetMd5(s string) string {
  data := []byte(s)
  mds := md5.Sum(data)
  md5str := fmt.Sprintf("%x", mds)
  return md5str
}

//检查错误的函数
func CheckErr(s string, err error) {
  if err != nil {
    fmt.Println(err)
    fmt.Println(s)
    os.Exit(0)
  }
}



func SwiWarnStatus(code int) int {
  switch code {
    case 1:
      return 99
    case 2:
      return 66
    default:
      return 66
  }
}




