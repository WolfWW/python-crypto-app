# Change Log
这篇更新日志用来练习写CHANGELOG，顺带记录软件的完善过程。

## [Unreleased]
### Changed
- 密钥文件、签名文件、源文件输入框改为只能通过浏览文件添加
### Added
- 对话框打印实时操作进度及耗时

## [1.2.0] - 2017-04-30
### Added
- 添加AES加密，可选择128、192、256位密钥，可自动生成密钥
- 添加RSA密钥文件生成和AES密钥位数的提示
### Changed
- 点击模式选择框就会清空其他所有输入框，且会根据模式显示对应的可选择项
- 现在签名时可以选择HASH算法了
- DES密钥和初始值不足8字符只会提示，不会清除；在密钥区没输入就切换焦点不会触发验证了
### Fixed
- 修复了必须点击其他输入框才会进行模式判断，现在选择后就会判断
- 修复对话框滚动条不随内容滚动的错误

## [1.1.2] - 2017-04-26
### Fixed
 - 修复未打印签名验证结果的BUG

## [1.1.1] - 2017-04-09
### Fixed
 - 修复不打印"生成密钥成功"的BUG
 - 修复操作成功后未清空输入框的BUG
 
## [1.1.0] - 2017-04-06
### Added
- 添加对DES密钥和初始值的验证
- 添加操作完成后清空所有输入框
### Fixed
- 修复点击选择模式时密钥文件输入框自动激活的BUG
 
## [1.0.0] - 2017-04-04
### Added
- 实现软件的UI界面操作
 
## [0.2.0] - 2017-04-02
### Changed
- 混合模式中不再需要手动输入DES密钥和初始值，改为随机生成，自动使用 
 
## 0.1.0 - 2017-04-01
- 初始命令行版本

[Unreleased]: https://github.com/WolfWW/python-crypto-app/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/WolfWW/python-crypto-app/compare/v1.1.2...v1.2.0
[1.1.2]: https://github.com/WolfWW/python-crypto-app/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/WolfWW/python-crypto-app/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/WolfWW/python-crypto-app/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/WolfWW/python-crypto-app/compare/v0.2.0...v1.0.0
[0.2.0]: https://github.com/WolfWW/python-crypto-app/compare/v0.1.0...v0.2.0