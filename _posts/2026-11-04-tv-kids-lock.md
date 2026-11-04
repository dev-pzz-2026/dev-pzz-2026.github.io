---
layout: post
title: TV儿童答题锁屏应用
categories: [工]
date: 2026-11-04
author: 半夏叁分
---

# TV儿童答题锁屏应用

一款专为电视（Android TV）设计的儿童锁屏应用：开机自动启动计时，到时锁屏，需答对题目才能解锁。用于家长控制儿童观看电视时长、教育机构限制娱乐时间等场景。

开源地址：<https://github.com/dev-pzz-2026/kidstvlock>

## 功能特性

- **答题解锁**：锁屏时显示汉字/题目，答对指定数量题目才能解锁。
- **开机自启**：电视开机后自动启动计时（默认开启）。
- **定时锁屏**：10 / 15 / 30 / 45 / 60 / 90 / 120 分钟可选，到时自动锁屏。
- **重启仍锁**：锁屏后即使关机重启，电视仍保持锁屏状态。
- **题库丰富**：内置 1-9 年级语文/数学/英语/科学题库及背诵篇目。
- **可配置**：通过 Web 配置页（端口 8080）调整参数，局域网访问 `http://<电视IP>:8080`。

## 源码结构

```
kidslock/
├── app/
│   ├── src/main/
│   │   ├── AndroidManifest.xml
│   │   ├── java/com/kidslock/app/
│   │   │   ├── MainActivity.java        # 设置界面
│   │   │   ├── LockScreenActivity.java  # 锁屏答题界面
│   │   │   ├── LockService.java         # 计时前台服务
│   │   │   ├── BootReceiver.java        # 开机自启动
│   │   │   ├── CharacterBank.java       # 题库加载
│   │   │   ├── PrefManager.java         # 设置持久化
│   │   │   ├── WebConfigServer.java     # Web 配置服务
│   │   │   └── WebConfigService.java    # Web 配置服务封装
│   │   ├── res/
│   │   │   ├── layout/                  # 布局 XML
│   │   │   ├── drawable/                # 按钮选择器、图标、TV banner
│   │   │   ├── mipmap-*/                # 启动图标
│   │   │   └── values/                  # 颜色、尺寸、字符串、主题
│   │   └── assets/                      # 题库 JSON
├── build.gradle
├── settings.gradle
├── gradle.properties
└── README.md
```

## 二次开发注意点

- 包名：`com.kidslock.app`。
- 默认观看时长：10 分钟（`PrefManager.DEFAULT_WATCH_LIMIT_MIN`）。
- 锁屏仅通过答题解锁，无家长 PIN / 密码入口。
- 常驻通知：`LockService` 前台服务，需通知权限。
- 开机自启：`BootReceiver` 监听 `BOOT_COMPLETED`。
- 题库：`assets/` 下 JSON，`CharacterBank` 解析。
- 修改图标：更新 `mipmap-*/ic_launcher*.png` 与 `drawable/tv_banner.png`（320×180）。
- 二次开发请保留 MIT 协议。

## 打包与安装

**环境**：JDK 17、Android SDK (API 34)、Gradle 8.2。

编译（Windows）：

```powershell
$env:JAVA_HOME="D:\data\Java\jdk-17.0.2"
$env:ANDROID_HOME="D:\data\Android\Sdk"
.\gradlew.bat assembleDebug --no-daemon
```

安装：将 APK 复制到 U 盘，插入电视 USB 口，在「高清播放器」或「文件管理」中找到 APK 安装；安装前需在电视「设置 → 账号与安全」中开启「允许安装未知来源应用」。或使用 adb：

```bash
adb connect <电视IP>:5555
adb install kidslock-release.apk
```

安装后需在电视设置中授予**开机自启、后台运行、悬浮窗**（部分机型）权限，建议将本应用加入白名单，避免被系统清理。

## 许可证

本项目采用 MIT License 开源，详见仓库 LICENSE 文件。

---

**开机自启 · 答题解锁**
