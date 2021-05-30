## 关于时区

### `cryptocompare.com`

`cryptocompare.com` 用的是timestamp，所以API调用与时区无关。

需要注意的是在其他网站（例如`tradingview.com`）看时间的时候需要设置为`UTC+9`，这样在用`pandas`读取时间的时候会默认系统时区。


## 一些问题

- 如何事先知道安装Python packages的时候需要用到哪些系统层面的Library？（例如：libgcc）
- 如何选择Python package的版本？
- VSCode连接上docker container中开发，无法识别import的库

```json
{
    "python.autoComplete.extraPaths": ["/usr/local/lib/python3.8/site-packages/"],
    "python.pythonPath": "/usr/local/bin/python3",
    "python.analysis.extraPaths": ["/usr/local/lib/python3.8/site-packages/"]
}
```

## 参考

- [Python development and production environment with debugging in Docker - Qiita](https://qiita.com/sebastianrettig/items/a52f6a5c36288db7b823)
- [Using Alpine can make Python Docker builds 50× slower](https://pythonspeed.com/articles/alpine-docker-python/)
- [Remote Python Development in Visual Studio Code | Python](https://devblogs.microsoft.com/python/remote-python-development-in-visual-studio-code/)
