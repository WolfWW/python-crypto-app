# Change Log
这篇更新日志用来练习写CHANGELOG，顺带记录软件的完善过程。

## [Unreleased]
### Changed
- 密钥文件、签名文件、源文件输入框改为只能通过浏览文件添加
### Added
- 对话框打印实时操作进度及耗时

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

[Unreleased]: https://github.com/WolfWW/python-crypto-app/compare/v1.1.1...HEAD
[1.1.1]: https://github.com/WolfWW/python-crypto-app/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/WolfWW/python-crypto-app/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/WolfWW/python-crypto-app/compare/v0.2.0...v1.0.0
[0.2.0]: https://github.com/WolfWW/python-crypto-app/compare/v0.1.0...v0.2.0