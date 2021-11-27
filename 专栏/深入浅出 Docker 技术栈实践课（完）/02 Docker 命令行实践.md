<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02 Docker 命令行实践.md</title>
        <!-- Spectre.css framework -->
        <link rel="stylesheet" href="../../static/index.css">
        <!-- theme css & js -->
        <meta name="generator" content="Hexo 4.2.0">
    </head>

<body>

<div class="book-container">
    <div class="book-sidebar">
        <div class="book-brand">
            <a href="../../index.html">
                <img src="../../static/favicon.png">
                <span>技术文章摘抄</span>
            </a>
        </div>
        <div class="book-menu uncollapsible">
            <ul class="uncollapsible">
                <li><a href="../../index.html" class="current-tab">首页</a></li>
            </ul>

            <ul class="uncollapsible">
                <li><a href="../index.html">上一级</a></li>
            </ul>

            <ul class="uncollapsible">
                <li>

                    
                    <a href="01&#32;导读：Docker&#32;核心技术预览.md">01 导读：Docker 核心技术预览.md</a>

                </li>
                <li>

                    <a class="current-tab" href="02&#32;Docker&#32;命令行实践.md">02 Docker 命令行实践.md</a>
                    

                </li>
                <li>

                    
                    <a href="03&#32;基于&#32;Docker&#32;的&#32;DevOps&#32;实践.md">03 基于 Docker 的 DevOps 实践.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;容器云平台的构建实践.md">04 容器云平台的构建实践.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;容器网络机制和多主机网络实践.md">05 容器网络机制和多主机网络实践.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;Docker&#32;日志机制与监控实践.md">06 Docker 日志机制与监控实践.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;自动化部署分布式容器云平台实践.md">07 自动化部署分布式容器云平台实践.md</a>

                </li>
            </ul>

        </div>
    </div>

    <div class="sidebar-toggle" onclick="sidebar_toggle()" onmouseover="add_inner()" onmouseleave="remove_inner()">
        <div class="sidebar-toggle-inner"></div>
    </div>

    <script>
        function add_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.add('show')
        }

        function remove_inner() {
            let inner = document.querySelector('.sidebar-toggle-inner')
            inner.classList.remove('show')
        }

        function sidebar_toggle() {
            let sidebar_toggle = document.querySelector('.sidebar-toggle')
            let sidebar = document.querySelector('.book-sidebar')
            let content = document.querySelector('.off-canvas-content')
            if (sidebar_toggle.classList.contains('extend')) { // show
                sidebar_toggle.classList.remove('extend')
                sidebar.classList.remove('hide')
                content.classList.remove('extend')
            } else { // hide
                sidebar_toggle.classList.add('extend')
                sidebar.classList.add('hide')
                content.classList.add('extend')
            }
        }
    </script>

    <div class="off-canvas-content">
        <div class="columns">
            <div class="column col-12 col-lg-12">
                <div class="book-navbar">
                    <!-- For Responsive Layout -->
                    <header class="navbar">
                        <section class="navbar-section">
                            <a onclick="open_sidebar()">
                                <i class="icon icon-menu"></i>
                            </a>
                        </section>
                    </header>
                </div>
                <div class="book-content" style="max-width: 960px; margin: 0 auto;
    overflow-x: auto;
    overflow-y: hidden;">
                    <div class="book-post">
                        <p id="tip" align="center"></p>
                        <div><h1>02 Docker 命令行实践</h1>
<p>Docker 官方为了让用户快速上手，提供了一个<a href="https://docs.docker.com/get-started/">交互式教程</a>，旨在帮助用户掌握 Docker 命令行的使用方法。但是由于 Docker 技术的快速发展，此交互式教程已经无法满足用户的实际使用需求，所以让我们一起开始一次真正的命令行学习之旅。</p>
<p>首先，Docker 的命令清单可以通过运行 <em>docker</em> ，或者 <em>docker help</em> 命令得到： <code>$ sudo docker</code>。</p>
<p><img src="assets/a151c870-b93b-11e7-b327-294b0b8e8fec" alt="enter image description here" /></p>
<p>在 Docker 容器技术不断演化的过程中，Docker 的子命令已经达到41个之多，其中核心子命令（例如：run）还会有复杂的参数配置。笔者通过结合功能和应用场景方面的考虑，把命令行划分为4个部分，方便我们快速概览 Docker 命令行的组成结构：</p>
<table>
<thead>
<tr>
<th align="left">功能划分</th>
<th align="left">命令</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">环境信息相关</td>
<td align="left">1. info 2. version</td>
</tr>
<tr>
<td align="left">系统运维相关</td>
<td align="left">1. attach 2. build 3. commit 4. cp 5. diff 6. images 7. export/ import / save / load 8. inspect 9. kill 10. port 11. pause / unpause 12. ps 13. rm 14. rmi 15. run 16. start / stop / restart 17. tag 18. top 19.wait 20. rename 21.stats 22. update 23. exec 24.deploy 25.create</td>
</tr>
<tr>
<td align="left">日志信息相关</td>
<td align="left">1. events 2. history 3. logs</td>
</tr>
<tr>
<td align="left">Docker Hub服务相关</td>
<td align="left">1. login/ logout 2. pull / push 3. search</td>
</tr>
</tbody>
</table>
<h4>参数约定</h4>
<p>单个字符的参数可以放在一起组合配置，例如：</p>
<pre><code class="language-bash">docker run -t -i --name test busybox sh 

</code></pre>
<p>可以用这样的方式等同：</p>
<pre><code class="language-bash">docker run -ti --name test busybox sh

</code></pre>
<h4>布尔值约定</h4>
<p>Boolean 参数形式如：-d=false。注意，当你声明这个 Boolean 参数时，比如 docker run -d=true，它将直接把启动的 Container 挂起放在后台运行。</p>
<h4>字符串和数字</h4>
<p>参数如 --name=“” 定义一个字符串，它仅能被定义一次。同类型的如-c=0 定义一个数字，它也只能被定义一次。</p>
<h4>后台进程</h4>
<p>Docker 后台进程是一个常驻后台的系统进程，目前已经从 Docker 程序分离处理一份独立的程序 dockerd 来执行守护后台进程。这个后台进程是用来启动容器引擎的，使用 dockerd --help 可以得到更详细的功能参数配置。如下图：</p>
<pre><code class="language-bash">Usage:    dockerd COMMAND

A self-sufficient runtime for containers.

Options:
      --add-runtime runtime                   Register an additional OCI compatible runtime (default [])
      --allow-nondistributable-artifacts list Push nondistributable artifacts to specified registries (default [])
      --api-cors-header string                Set CORS headers in the Engine API
      --authorization-plugin list             Authorization plugins to load (default [])
      --bip string                            Specify network bridge IP
  -b, --bridge string                         Attach containers to a network bridge
      --cgroup-parent string                  Set parent cgroup for all containers
      --cluster-advertise string              Address or interface name to advertise
      --cluster-store string                  URL of the distributed storage backend
      --cluster-store-opt map                 Set cluster store options (default map[])
      --config-file string                    Daemon configuration file (default &quot;/etc/docker/daemon.json&quot;)
      --containerd string                     Path to containerd socket
      --cpu-rt-period int                     Limit the CPU real-time period in microseconds
      --cpu-rt-runtime int                    Limit the CPU real-time runtime in microseconds
      --data-root string                      Root directory of persistent Docker state (default &quot;/var/lib/docker&quot;)
  -D, --debug                                 Enable debug mode
      --default-gateway ip                    Container default gateway IPv4 address
      --default-gateway-v6 ip                 Container default gateway IPv6 address
      --default-runtime string                Default OCI runtime for containers (default &quot;runc&quot;)
      --default-ulimit ulimit                 Default ulimits for containers (default [])
      --disable-legacy-registry               Disable contacting legacy registries (default true)
      --dns list                              DNS server to use (default [])
      --dns-opt list                          DNS options to use (default [])
      --dns-search list                       DNS search domains to use (default [])
      --exec-opt list                         Runtime execution options (default [])
      --exec-root string                      Root directory for execution state files (default &quot;/var/run/docker&quot;)
      --experimental                          Enable experimental features
      --fixed-cidr string                     IPv4 subnet for fixed IPs
      --fixed-cidr-v6 string                  IPv6 subnet for fixed IPs
  -G, --group string                          Group for the unix socket (default &quot;docker&quot;)
      --help                                  Print usage
  -H, --host list                             Daemon socket(s) to connect to (default [])
      --icc                                   Enable inter-container communication (default true)
      --init                                  Run an init in the container to forward signals and reap processes
      --init-path string                      Path to the docker-init binary
      --insecure-registry list                Enable insecure registry communication (default [])
      --ip ip                                 Default IP when binding container ports (default 0.0.0.0)
      --ip-forward                            Enable net.ipv4.ip_forward (default true)
      --ip-masq                               Enable IP masquerading (default true)
      --iptables                              Enable addition of iptables rules (default true)
      --ipv6                                  Enable IPv6 networking
      --label list                            Set key=value labels to the daemon (default [])
      --live-restore                          Enable live restore of docker when containers are still running
      --log-driver string                     Default driver for container logs (default &quot;json-file&quot;)
  -l, --log-level string                      Set the logging level (&quot;debug&quot;, &quot;info&quot;, &quot;warn&quot;, &quot;error&quot;, &quot;fatal&quot;) (default &quot;info&quot;)
      --log-opt map                           Default log driver options for containers (default map[])
      --max-concurrent-downloads int          Set the max concurrent downloads for each pull (default 3)
      --max-concurrent-uploads int            Set the max concurrent uploads for each push (default 5)
      --metrics-addr string                   Set default address and port to serve the metrics api on
      --mtu int                               Set the containers network MTU
      --no-new-privileges                     Set no-new-privileges by default for new containers
      --oom-score-adjust int                  Set the oom_score_adj for the daemon (default -500)
  -p, --pidfile string                        Path to use for daemon PID file (default &quot;/var/run/docker.pid&quot;)
      --raw-logs                              Full timestamps without ANSI coloring
      --registry-mirror list                  Preferred Docker registry mirror (default [])
      --seccomp-profile string                Path to seccomp profile
      --selinux-enabled                       Enable selinux support
      --shutdown-timeout int                  Set the default shutdown timeout (default 15)
  -s, --storage-driver string                 Storage driver to use
      --storage-opt list                      Storage driver options (default [])
      --swarm-default-advertise-addr string   Set default address or interface for swarm advertised address
      --tls                                   Use TLS; implied by --tlsverify
      --tlscacert string                      Trust certs signed only by this CA (default &quot;~/.docker/ca.pem&quot;)
      --tlscert string                        Path to TLS certificate file (default &quot;~/.docker/cert.pem&quot;)
      --tlskey string                         Path to TLS key file (default ~/.docker/key.pem&quot;)
      --tlsverify                             Use TLS and verify the remote
      --userland-proxy                        Use userland proxy for loopback traffic (default true)
      --userland-proxy-path string            Path to the userland proxy binary
      --userns-remap string                   User/Group setting for user namespaces
  -v, --version                               Print version information and qui

</code></pre>
<p>Docker 后台进程参数清单如下表：</p>
<table>
<thead>
<tr>
<th align="left">参数</th>
<th align="left">解释</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">--add-runtime runtime</td>
<td align="left">选择容器运行时引擎，默认 containerd</td>
</tr>
<tr>
<td align="left">--allow-nondistributable-artifacts list</td>
<td align="left">因为类如 window base image 包含版权限制，所以配置指定的私有镜像仓库，可以帮助应用正常发布</td>
</tr>
<tr>
<td align="left">--api-cors-header string</td>
<td align="left">提供跨站 API 请求自定义包头信息</td>
</tr>
<tr>
<td align="left">--authorization-plugin list</td>
<td align="left">认证插件配置</td>
</tr>
<tr>
<td align="left">--bip string</td>
<td align="left">配置网桥地址</td>
</tr>
<tr>
<td align="left">-b, --bridge string</td>
<td align="left">连接网桥</td>
</tr>
<tr>
<td align="left">--cgroup-parent string</td>
<td align="left">配置容器的父 cgroup 信息</td>
</tr>
<tr>
<td align="left">--cluster-advertise string</td>
<td align="left">集群广播网络地址</td>
</tr>
<tr>
<td align="left">--cluster-store string</td>
<td align="left">集群存储支持</td>
</tr>
<tr>
<td align="left">--cluster-store-opt map</td>
<td align="left">集群存储参数配置</td>
</tr>
<tr>
<td align="left">--config-file string</td>
<td align="left">后台引擎参数配置文件</td>
</tr>
<tr>
<td align="left">--containerd string</td>
<td align="left">容器引擎实例网络套接字路径</td>
</tr>
<tr>
<td align="left">--cpu-rt-period int</td>
<td align="left">限制 CPU 间隔频率（微秒级别）</td>
</tr>
<tr>
<td align="left">--cpu-rt-runtime int</td>
<td align="left">限制 CPU 运行时频率（微秒级别）</td>
</tr>
<tr>
<td align="left">--data-root string</td>
<td align="left">容器引擎数据根目录地址</td>
</tr>
<tr>
<td align="left">-D, --debug</td>
<td align="left">调试信息</td>
</tr>
<tr>
<td align="left">--default-gateway ip</td>
<td align="left">容器默认 IPv4 网络网关</td>
</tr>
<tr>
<td align="left">--default-gateway-v6 ip</td>
<td align="left">容器默认 IPv6 网络网关</td>
</tr>
<tr>
<td align="left">--default-runtime string</td>
<td align="left">容器运行时，默认 runc</td>
</tr>
<tr>
<td align="left">--default-ulimit ulimit</td>
<td align="left">配置容器默认最大文件限制数，改善运行性能</td>
</tr>
<tr>
<td align="left">--disable-legacy-registry</td>
<td align="left">废弃老版本镜像仓库</td>
</tr>
<tr>
<td align="left">--dns list</td>
<td align="left">DNS 服务地址</td>
</tr>
<tr>
<td align="left">--dns-opt list</td>
<td align="left">DNS 服务参数</td>
</tr>
<tr>
<td align="left">--dns-search list</td>
<td align="left">DNS服务查询域名配置</td>
</tr>
<tr>
<td align="left">--exec-opt list</td>
<td align="left">运行时执行参数</td>
</tr>
<tr>
<td align="left">--exec-root string</td>
<td align="left">运行时执行根目录地址</td>
</tr>
<tr>
<td align="left">--experimental</td>
<td align="left">启用实验性特性</td>
</tr>
<tr>
<td align="left">--fixed-cidr string</td>
<td align="left">固定 IPv4 网段</td>
</tr>
<tr>
<td align="left">--fixed-cidr-v6 string</td>
<td align="left">固定 IPv6 网段</td>
</tr>
<tr>
<td align="left">-G, --group string</td>
<td align="left">网络套接字所属组</td>
</tr>
<tr>
<td align="left">--help</td>
<td align="left">帮助信息</td>
</tr>
<tr>
<td align="left">-H, --host list</td>
<td align="left">后台进程连接地址</td>
</tr>
<tr>
<td align="left">--icc</td>
<td align="left">启用容器间的网络互联，默认启用</td>
</tr>
<tr>
<td align="left">--init</td>
<td align="left">在容器运行时启动一个 init 程序，来统一管理进程</td>
</tr>
<tr>
<td align="left">--init-path string</td>
<td align="left">docker init 的路径地址</td>
</tr>
<tr>
<td align="left">--insecure-registry list</td>
<td align="left">非安全镜像仓库地址列表</td>
</tr>
<tr>
<td align="left">--ip ip</td>
<td align="left">默认容器绑定 IP 地址，默认 0.0.0.0</td>
</tr>
<tr>
<td align="left">--ip-forward</td>
<td align="left">启动 net.ipv4.ip_forward</td>
</tr>
<tr>
<td align="left">--ip-masq</td>
<td align="left">启动IP混淆</td>
</tr>
<tr>
<td align="left">--iptables</td>
<td align="left">启动默认的iptable规则</td>
</tr>
<tr>
<td align="left">--ipv6</td>
<td align="left">启动 IPv6 网络</td>
</tr>
<tr>
<td align="left">--label list</td>
<td align="left">配置键值对参数到引擎后台</td>
</tr>
<tr>
<td align="left">--live-restore</td>
<td align="left">启用容器热迁移特性</td>
</tr>
<tr>
<td align="left">--log-driver string</td>
<td align="left">日志驱动配置，默认 json-file</td>
</tr>
<tr>
<td align="left">-l, --log-level string</td>
<td align="left">日志级别</td>
</tr>
<tr>
<td align="left">--log-opt map</td>
<td align="left">日志驱动参数</td>
</tr>
<tr>
<td align="left">--max-concurrent-downloads int</td>
<td align="left">每次 pull 的最大下载线程数</td>
</tr>
<tr>
<td align="left">--max-concurrent-uploads int</td>
<td align="left">每次 push 最大上传线程数</td>
</tr>
<tr>
<td align="left">--metrics-addr string</td>
<td align="left">监控地址</td>
</tr>
<tr>
<td align="left">--mtu int</td>
<td align="left">网络数据包 MTU 配置</td>
</tr>
<tr>
<td align="left">--no-new-privileges</td>
<td align="left">去掉 no<em>new</em>privs 权限</td>
</tr>
<tr>
<td align="left">--oom-score-adjust int</td>
<td align="left">OOM 阈值配置</td>
</tr>
<tr>
<td align="left">-p, --pidfile string</td>
<td align="left">引擎后台进程文件地址</td>
</tr>
<tr>
<td align="left">--raw-logs</td>
<td align="left">无 ANSI 颜色的日志</td>
</tr>
<tr>
<td align="left">--registry-mirror list</td>
<td align="left">镜像仓库同步镜像地址</td>
</tr>
<tr>
<td align="left">--seccomp-profile string</td>
<td align="left">seccomp 文件地址</td>
</tr>
<tr>
<td align="left">--selinux-enabled</td>
<td align="left">启用 selinux</td>
</tr>
<tr>
<td align="left">--shutdown-timeout int</td>
<td align="left">默认停机超时时间，默认15 秒</td>
</tr>
<tr>
<td align="left">-s, --storage-driver string</td>
<td align="left">容器存储驱动</td>
</tr>
<tr>
<td align="left">--storage-opt list</td>
<td align="left">容器存储驱动参数</td>
</tr>
<tr>
<td align="left">--swarm-default-advertise-addr string</td>
<td align="left">swarm 集群广播地址</td>
</tr>
<tr>
<td align="left">--tls</td>
<td align="left">使用 TLS 认证</td>
</tr>
<tr>
<td align="left">--tlscacert string</td>
<td align="left">CA 文件地址</td>
</tr>
<tr>
<td align="left">--tlscert string</td>
<td align="left">TLS 认证文件地址</td>
</tr>
<tr>
<td align="left">--tlskey string</td>
<td align="left">TLS 私钥地址</td>
</tr>
<tr>
<td align="left">--tlsverify</td>
<td align="left">使用 TLS 认证</td>
</tr>
<tr>
<td align="left">--userland-proxy</td>
<td align="left">使用用户态 proxy 来路由 loopback 流量</td>
</tr>
<tr>
<td align="left">--userland-proxy-path string</td>
<td align="left">用户态 proxy 地址</td>
</tr>
<tr>
<td align="left">--userns-remap string</td>
<td align="left">用户命令空间的用户、用户组配置</td>
</tr>
<tr>
<td align="left">-v, --version</td>
<td align="left">版本</td>
</tr>
</tbody>
</table>
<h3>Docker 命令行探秘</h3>
<h4>环境信息相关</h4>
<p><strong>info</strong></p>
<p>使用方法：docker info</p>
<p>例子：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="711714151e031031151e121a14035c151407141d5c121d18">[email&#160;protected]</a> docker]$ sudo docker -D info
Containers: 0
Images: 32
Storage Driver: devicemapper
 Pool Name: docker-252:1-130159-pool
 Data file: /var/lib/docker/devicemapper/devicemapper/data
 Metadata file: /var/lib/docker/devicemapper/devicemapper/metadata
 Data Space Used: 1616.9 Mb
 Data Space Total: 102400.0 Mb
 Metadata Space Used: 2.4 Mb
 Metadata Space Total: 2048.0 Mb
Execution Driver: native-0.2
Kernel Version: 3.11.10-301.fc20.x86_64
Debug mode (server): false
Debug mode (client): true
Fds: 11
Goroutines: 14
EventsListeners: 0
Init SHA1: 2c5adb59737b8a01fa3fb968519a43fe140bc9c9
Init Path: /usr/libexec/docker/dockerinit
Sockets: [fd://]

</code></pre>
<p>使用说明：</p>
<p>这个命令在开发者报告 Bug 时会非常有用，结合 docker vesion 一起，可以随时使用这个命令把本地的配置信息提供出来，方便 Docker 的开发者快速定位问题。</p>
<p><strong>version</strong></p>
<p>使用方法：docker version</p>
<p>使用说明：</p>
<p>显示 Docker 的版本号，API 版本号，Git commit，Docker 客户端和后台进程的 Go 版本号。</p>
<h4>系统运维相关</h4>
<p><strong>attach</strong></p>
<p>使用方法：docker attach [OPTIONS] CONTAINER</p>
<p>例子：</p>
<pre><code>$ ID=$(sudo docker run -d ubuntu /usr/bin/top -b)
$ sudo docker attach $ID
top - 17:21:49 up  5:53,  0 users,  load average: 0.63, 1.15, 0.78
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.0 us,  0.7 sy,  0.0 ni, 97.7 id,  0.7 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:   2051644 total,   723700 used,  1327944 free,    33032 buffers
KiB Swap:   0 total,   0 used,  0 free.   565836 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND
    1 root      20   0   19748   1280   1008 R  0.0  0.1   0:00.04 top
$ sudo docker stop $ID

</code></pre>
<p>使用说明：</p>
<p>使用这个命令可以挂载正在后台运行的容器，在开发应用的过程中运用这个命令可以随时观察容器內进程的运行状况。开发者在开发应用的场景中，这个命令是一个非常有用的命令。</p>
<p><strong>build</strong></p>
<p>使用方法：docker build [OPTIONS] PATH | URL | -</p>
<p>例子：</p>
<pre><code>$ docker build .
Uploading context 18.829 MB
Uploading context
Step 0 : FROM busybox
 ---&gt; 769b9341d937
Step 1 : CMD echo Hello world
 ---&gt; Using cache
 ---&gt; 99cc1ad10469
Successfully built 99cc1ad10469

</code></pre>
<p>使用说明：</p>
<p>这个命令是从源码构建新 Image 的命令。因为 Image 是分层的，最关键的 Base Image 是如何构建的是用户比较关心的，Docker 官方文档给出了构建方法，请参考<a href="https://docs.docker.com/engine/userguide/eng-image/baseimages/">这里</a>。</p>
<p><strong>commit</strong></p>
<p>使用方法：docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]</p>
<p>例子：</p>
<pre><code>$ sudo docker ps
ID                  IMAGE               COMMAND             CREATED             STATUS              PORTS
c3f279d17e0a        ubuntu:12.04        /bin/bash           7 days ago          Up 25 hours
197387f1b436        ubuntu:12.04        /bin/bash           7 days ago          Up 25 hours
$ docker commit c3f279d17e0a  SvenDowideit/testimage:version3
f5283438590d
$ docker images | head
REPOSITORY                        TAG                 ID                  CREATED             VIRTUAL SIZE
SvenDowideit/testimage            version3            f5283438590d        16 seconds ago      335.7 MB

</code></pre>
<p>使用说明：</p>
<p>这个命令的用处在于把有修改的 container 提交成新的 Image，然后导出此 Imange 分发给其他场景中调试使用。Docker 官方的建议是，当你在调试完 Image 的问题后，应该写一个新的 Dockerfile 文件来维护此 Image。commit 命令仅是一个临时创建 Imange 的辅助命令。</p>
<p><strong>cp</strong></p>
<p>使用方法： cp CONTAINER:PATH HOSTPATH</p>
<p>使用说明：</p>
<p>使用 cp 可以把容器內的文件复制到 Host 主机上。这个命令在开发者开发应用的场景下，会需要把运行程序产生的结果复制出来的需求，在这个情况下就可以使用这个 cp 命令。</p>
<p><strong>diff</strong></p>
<p>使用方法：docker diff CONTAINER</p>
<p>例子：</p>
<pre><code>$ sudo docker diff 7bb0e258aefe

C /dev
A /dev/kmsg
C /etc
A /etc/mtab
A /go
A /go/src
A /go/src/github.com
A /go/src/github.com/dotcloud
....

</code></pre>
<p>使用说明：</p>
<p>diff 会列出3种容器内文件状态变化（A - Add，D - Delete，C - Change）的列表清单。构建Image的过程中需要的调试指令。</p>
<p><strong>images</strong></p>
<p>使用方法：docker images [OPTIONS] [NAME]</p>
<p>例子：</p>
<pre><code>$ sudo docker images | head
REPOSITORY TAG IMAGE ID CREATED VIRTUAL SIZE
&lt;none&gt; &lt;none&gt; 77af4d6b9913 19 hours ago 1.089 GB
committest latest b6fa739cedf5 19 hours ago 1.089 GB
&lt;none&gt; &lt;none&gt; 78a85c484f71 19 hours ago 1.089 GB
$ docker latest 30557a29d5ab 20 hours ago 1.089 GB
&lt;none&gt; &lt;none&gt; 0124422dd9f9 20 hours ago 1.089 GB
&lt;none&gt; &lt;none&gt; 18ad6fad3402 22 hours ago 1.082 GB
&lt;none&gt; &lt;none&gt; f9f1e26352f0 23 hours ago 1.089 GB
tryout latest 2629d1fa0b81 23 hours ago 131.5 MB
&lt;none&gt; &lt;none&gt; 5ed6274db6ce 24 hours ago 1.089 GB

</code></pre>
<p>使用说明：</p>
<p>Docker Image 是多层结构的，默认只显示最顶层的 Image。不显示的中间层默认是为了增加可复用性、减少磁盘使用空间，加快 build 构建的速度的功能，一般用户不需要关心这个细节。</p>
<p><strong>export/ import / save / load</strong></p>
<p>使用方法：</p>
<pre><code class="language-bash">docker export red_panda &gt; latest.tar
docker import URL|- [REPOSITORY[:TAG]]
docker save IMAGE
docker load

</code></pre>
<p>使用说明：</p>
<p>这一组命令是系统运维里非常关键的命令。加载（两种方法：import，load），导出（一种方法：save，export）容器系统文件。</p>
<p><strong>inspect</strong></p>
<p>使用方法：</p>
<pre><code>docker inspect CONTAINER|IMAGE [CONTAINER|IMAGE...]

</code></pre>
<p>例子：</p>
<pre><code>$ sudo docker inspect --format='{{.NetworkSettings.IPAddress}}' $INSTANCE_ID

</code></pre>
<p>使用说明：</p>
<p>查看容器运行时详细信息的命令。了解一个 Image 或者 Container 的完整构建信息就可以通过这个命令实现。</p>
<p><strong>kill</strong></p>
<p>使用方法：</p>
<pre><code>docker kill [OPTIONS] CONTAINER [CONTAINER...]

</code></pre>
<p>使用说明：</p>
<p>杀掉容器的进程。</p>
<p><strong>port</strong></p>
<p>使用方法：</p>
<pre><code>docker port CONTAINER PRIVATE_PORT

</code></pre>
<p>使用说明：</p>
<p>打印出 Host 主机端口与容器暴露出的端口的 NAT 映射关系</p>
<p><strong>pause / unpause</strong></p>
<p>使用方法：</p>
<pre><code>docker pause CONTAINER

</code></pre>
<p>使用说明：</p>
<p>使用 cgroup 的 freezer 顺序暂停、恢复容器里的所有进程。详细 freezer 的特性，请参考<a href="https://www.kernel.org/doc/Documentation/cgroup-v1/freezer-subsystem.txt">官方文档</a>。</p>
<p><strong>ps</strong></p>
<p>使用方法：</p>
<pre><code>docker ps [OPTIONS]

</code></pre>
<p>例子：</p>
<pre><code>$ docker ps
CONTAINER ID        IMAGE                        COMMAND                CREATED              STATUS              PORTS               NAMES
4c01db0b339c        ubuntu:12.04                 bash                   17 seconds ago       Up 16 seconds                           webapp
d7886598dbe2        crosbymichael/redis:latest   /redis-server --dir    33 minutes ago       Up 33 minutes       6379/tcp            redis,webapp/db

</code></pre>
<p>使用说明：</p>
<p>docker ps 打印出正在运行的容器，docker ps -a 打印出所有运行过的容器。</p>
<p><strong>rm</strong></p>
<p>使用方法：</p>
<pre><code>docker rm [OPTIONS] CONTAINER [CONTAINER...]

</code></pre>
<p>例子：</p>
<pre><code>$ sudo docker rm /redis
/redis

</code></pre>
<p>使用说明：</p>
<p>删除指定的容器。</p>
<p><strong>rmi</strong></p>
<p>使用方法：</p>
<pre><code>docker rmi IMAGE [IMAGE...]

</code></pre>
<p>例子：</p>
<pre><code>$ sudo docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
test1 latest fd484f19954f 23 seconds ago 7 B (virtual 4.964 MB)
test latest fd484f19954f 23 seconds ago 7 B (virtual 4.964 MB)
test2 latest fd484f19954f 23 seconds ago 7 B (virtual 4.964 MB)

$ sudo docker rmi fd484f19954f
Error: Conflict, cannot delete image fd484f19954f because it is tagged in multiple repositories
2013/12/11 05:47:16 Error: failed to remove one or more images

$ sudo docker rmi test1
Untagged: fd484f19954f4920da7ff372b5067f5b7ddb2fd3830cecd17b96ea9e286ba5b8

$ sudo docker rmi test2
Untagged: fd484f19954f4920da7ff372b5067f5b7ddb2fd3830cecd17b96ea9e286ba5b8

$ sudo docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
test latest fd484f19954f 23 seconds ago 7 B (virtual 4.964 MB)

$ sudo docker rmi test
Untagged: fd484f19954f4920da7ff372b5067f5b7ddb2fd3830cecd17b96ea9e286ba5b8
Deleted: fd484f19954f4920da7ff372b5067f5b7ddb2fd3830cecd17b96ea9e286ba5b8

</code></pre>
<p>使用说明：</p>
<p>指定删除 Image 文件。</p>
<p><strong>run</strong></p>
<p>使用方法：</p>
<pre><code>docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

</code></pre>
<p>例子：</p>
<pre><code>$ sudo docker run --cidfile /tmp/docker_test.cid ubuntu echo &quot;test&quot;

</code></pre>
<p>使用说明：</p>
<p>这个命令是核心命令，可以配置的子参数详细解释可以通过 docker run --help 列出。</p>
<p><strong>start / stop / restart</strong></p>
<p>使用方法：</p>
<pre><code>docker start CONTAINER [CONTAINER...]

</code></pre>
<p>使用说明：</p>
<p>这组命令可以开启（两个：start，restart），停止（一个：stop）一个容器。</p>
<p><strong>tag</strong></p>
<p>使用方法：</p>
<pre><code>docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]

</code></pre>
<p>使用说明：</p>
<p>组合使用用户名，Image 名字，标签名来组织管理Image。</p>
<p><strong>top</strong></p>
<p>使用方法：</p>
<pre><code>docker top CONTAINER [ps OPTIONS]

</code></pre>
<p>使用说明：</p>
<p>显示容器內运行的进程。</p>
<p><strong>wait</strong></p>
<p>使用方法：</p>
<pre><code>docker wait CONTAINER [CONTAINER...]

</code></pre>
<p>使用说明：</p>
<p>阻塞对指定容器的其他调用方法，直到容器停止后退出阻塞。</p>
<p><strong>rename</strong></p>
<p>使用方法：</p>
<pre><code>docker rename CONTAINER NEW_NAME

</code></pre>
<p>使用说明：</p>
<p>重新命名一个容器。</p>
<p><strong>stats</strong></p>
<p>使用方法：</p>
<pre><code>docker stats [OPTIONS] [CONTAINER...]

</code></pre>
<p>使用说明：</p>
<p>实时显示容器资源使用监控指标。</p>
<p><strong>update</strong></p>
<p>使用方法：</p>
<pre><code>docker update [OPTIONS] CONTAINER [CONTAINER...]

</code></pre>
<p>使用说明：</p>
<p>更新一或多个容器实例的 IO、CPU、内存，启动策略参数。</p>
<p><strong>exec</strong></p>
<p>使用方法：</p>
<pre><code>docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

</code></pre>
<p>使用说明：</p>
<p>在运行中容器中运行命令。</p>
<p><strong>deploy</strong></p>
<p>使用方法：</p>
<pre><code>docker deploy [OPTIONS] STACK

</code></pre>
<p>使用说明：</p>
<p>部署新的 stack 文件，两种格式 DAB 格式和 Compose 格式，当前使用趋势来看，Compose 成为默认标准。</p>
<p><strong>create</strong></p>
<p>使用方法：</p>
<pre><code>docker create [OPTIONS] IMAGE [COMMAND] [ARG...]

</code></pre>
<p>使用说明：</p>
<p>这是一个重要的命令，可以创建容器但并不执行它。</p>
<h4>日志信息相关</h4>
<p><strong>events</strong></p>
<p>使用方法：</p>
<pre><code>docker events [OPTIONS]

</code></pre>
<p>使用说明：</p>
<p>打印容器实时的系统事件。</p>
<p><strong>history</strong></p>
<p>使用方法：</p>
<pre><code>docker history [OPTIONS] IMAGE

</code></pre>
<p>例子：</p>
<pre><code class="language-bash">$ docker history docker
IMAGE CREATED CREATED BY SIZE
3e23a5875458790b7a806f95f7ec0d0b2a5c1659bfc899c89f939f6d5b8f7094 8 days ago 
/bin/sh -c #(nop) ENV LC_ALL=C.UTF-8 0 B
8578938dd17054dce7993d21de79e96a037400e8d28e15e7290fea4f65128a36 8 days ago 
/bin/sh -c dpkg-reconfigure locales &amp;&amp; locale-gen C.UTF-8 &amp;&amp; 
/usr/sbin/update-locale LANG=C.UTF-8 1.245 MB
be51b77efb42f67a5e96437b3e102f81e0a1399038f77bf28cea0ed23a65cf60 8 days ago /bin/sh 
-c apt-get update &amp;&amp; apt-get install -y git libxml2-dev python build-essential 
make gcc python-dev locales python-pip 338.3 MB
4b137612be55ca69776c7f30c2d2dd0aa2e7d72059820abf3e25b629f887a084 6 weeks ago 
/bin/sh -c #(nop) ADD jessie.tar.xz in / 121 MB
750d58736b4b6cc0f9a9abe8f258cef269e3e9dceced1146503522be9f985ada 6 weeks ago 
/bin/sh -c #(nop) MAINTAINER Tianon Gravi &lt;<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="2140454c56484646484f61464c40484d0f424e4c">[email&#160;protected]</a>&gt;
 - mkimage-debootstrap.sh -t jessie.tar.xz jessie http://http.debian.net/debian 0 B
511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158 9 months ago 0 B

</code></pre>
<p>使用说明：</p>
<p>打印指定 Image 中每一层 Image 命令行的历史记录。</p>
<p><strong>logs</strong></p>
<p>使用方法：</p>
<pre><code>docker logs CONTAINER

</code></pre>
<p>使用说明：</p>
<p>批量打印出容器中进程的运行日志。</p>
<h4>Hub服务相关</h4>
<p><strong>login/ logout</strong></p>
<p>使用方法：</p>
<pre><code>docker login [OPTIONS] [SERVER]
docker logout [SERVER]

</code></pre>
<p>使用说明：</p>
<p>登录登出 Docker Hub 服务。</p>
<p><strong>pull / push</strong></p>
<p>使用方法：</p>
<pre><code>docker push NAME[:TAG]

</code></pre>
<p>使用说明：</p>
<p>通过此命令分享 Image 到 Hub 服务或者自服务的 Registry 服务。</p>
<p><strong>search</strong></p>
<p>使用方法：</p>
<pre><code>docker search TERM

</code></pre>
<p>使用说明：</p>
<p>通过关键字搜索分享的 Image。</p>
<h3>总结</h3>
<p>通过以上 Docker 命令行的详细解释，可以强化对 Docker 命令的全面理解。考虑到 Docker 命令行的发展变化非常快，读者可以参考官方的<a href="https://docs.docker.com/engine/reference/run/">命令行解释</a>文档更新相应的命令行解释。另外，通过以上 Docker 命令行的分析，可以知道 Docker 命令行架构设计的特点在于客户端和服务端的运行文件是同一个文件，内部实现代码应该是重用的设计。笔者希望开发者在开发类似的命令行应用时参考这样的设计，减少前后台容错的复杂度。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;导读：Docker&#32;核心技术预览.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;基于&#32;Docker&#32;的&#32;DevOps&#32;实践.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43584e9fc4645f","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
</body>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NPSEEVD756"></script>
<script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
        dataLayer.push(arguments);
    }

    gtag('js', new Date());
    gtag('config', 'G-NPSEEVD756');
    var path = window.location.pathname
    var cookie = getCookie("lastPath");
    console.log(path)
    if (path.replace("/", "") === "") {
        if (cookie.replace("/", "") !== "") {
            console.log(cookie)
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/%E6%B7%B1%E5%85%A5%E6%B5%85%E5%87%BA%20Docker%20%E6%8A%80%E6%9C%AF%E6%A0%88%E5%AE%9E%E8%B7%B5%E8%AF%BE%EF%BC%88%E5%AE%8C%EF%BC%89/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
        }
    } else {
        setCookie("lastPath", path)
    }

    function setCookie(cname, cvalue) {
        var d = new Date();
        d.setTime(d.getTime() + (180 * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + "; " + expires + ";path = /";
    }

    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i].trim();
            if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
        }
        return "";
    }
</script>

</html>
