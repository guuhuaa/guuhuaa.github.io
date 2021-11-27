<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>05 动手实践：搭建一个 Kubernetes 集群 - 生产可用.md</title>
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

                    
                    <a href="01&#32;&#32;开篇：&#32;Kubernetes&#32;是什么以及为什么需要它.md">01  开篇： Kubernetes 是什么以及为什么需要它.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;初步认识：Kubernetes&#32;基础概念.md">02 初步认识：Kubernetes 基础概念.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;宏观认识：整体架构.md">03 宏观认识：整体架构.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;搭建&#32;Kubernetes&#32;集群&#32;-&#32;本地快速搭建.md">04 搭建 Kubernetes 集群 - 本地快速搭建.md</a>

                </li>
                <li>

                    <a class="current-tab" href="05&#32;动手实践：搭建一个&#32;Kubernetes&#32;集群&#32;-&#32;生产可用.md">05 动手实践：搭建一个 Kubernetes 集群 - 生产可用.md</a>
                    

                </li>
                <li>

                    
                    <a href="06&#32;集群管理：初识&#32;kubectl.md">06 集群管理：初识 kubectl.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;集群管理：以&#32;Redis&#32;为例-部署及访问.md">07 集群管理：以 Redis 为例-部署及访问.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;安全重点&#32;认证和授权.md">08 安全重点 认证和授权.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;应用发布：部署实际项目.md">09 应用发布：部署实际项目.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;应用管理：初识&#32;Helm.md">10 应用管理：初识 Helm.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;部署实践：以&#32;Helm&#32;部署项目.md">11 部署实践：以 Helm 部署项目.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;庖丁解牛：kube-apiserver.md">12 庖丁解牛：kube-apiserver.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;庖丁解牛：etcd.md">13 庖丁解牛：etcd.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;庖丁解牛：controller-manager.md">14 庖丁解牛：controller-manager.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;庖丁解牛：kube-scheduler.md">15 庖丁解牛：kube-scheduler.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;庖丁解牛：kubelet.md">16 庖丁解牛：kubelet.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;庖丁解牛：kube-proxy.md">17 庖丁解牛：kube-proxy.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;庖丁解牛：Container&#32;Runtime&#32;（Docker）.md">18  庖丁解牛：Container Runtime （Docker）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Troubleshoot.md">19 Troubleshoot.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;扩展增强：Dashboard.md">20 扩展增强：Dashboard.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;扩展增强：CoreDNS.md">21 扩展增强：CoreDNS.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;服务增强：Ingress.md">22 服务增强：Ingress.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;监控实践：对&#32;K8S&#32;集群进行监控.md">23 监控实践：对 K8S 集群进行监控.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;总结.md">24 总结.md</a>

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
                        <div><h1>05 动手实践：搭建一个 Kubernetes 集群 - 生产可用</h1>
<p>通过上一节的学习，我们快速的使用 <code>Minikube</code> 搭建了一个本地可用的 K8S 集群。默认情况下，节点是一个虚拟机实例，我们可以在上面体验一些基本的功能。</p>
<p>大多数人的需求并不只是包含一个虚拟机节点的本地测试集群，而是一个可在服务器运行，可自行扩/缩容，具备全部功能的，达到生产可用的集群。</p>
<p>K8S 集群的搭建，一直让很多人头疼，本节我们来搭建一个生产可用的集群，便于后续的学习或使用。</p>
<h2>方案选择</h2>
<p>K8S 生产环境可用的集群方案有很多，本节我们选择一个 Kubernetes 官方推荐的方案 <code>kubeadm</code> 进行搭建。</p>
<p><code>kubeadm</code> 是 Kubernetes 官方提供的一个 CLI 工具，可以很方便的搭建一套符合官方最佳实践的最小化可用集群。当我们使用 <code>kubeadm</code> 搭建集群时，集群可以通过 K8S 的一致性测试，并且 <code>kubeadm</code> 还支持其他的集群生命周期功能，比如升级/降级等。</p>
<p>我们在此处选择 <code>kubeadm</code> ，因为我们可以不用过于关注集群的内部细节，便可以快速的搭建出生产可用的集群。我们可以通过后续章节的学习，快速上手 K8S ，并学习到 K8S 的内部原理。在此基础上，想要在物理机上完全一步步搭建集群，便轻而易举。</p>
<h2>安装基础组件</h2>
<h3>前期准备</h3>
<p>使用 <code>kubeadm</code> 前，我们需要提前做一些准备。</p>
<ul>
<li>
<p><strong>我们需要禁用 swap</strong>。通过之前的学习，我们知道每个节点上都有个必须的组件，名为 <code>kubelet</code>，自 K8S 1.8 开始，启动 <code>kubelet</code> 时，需要禁用 <code>swap</code> 。或者需要更改 <code>kubelet</code> 的启动参数 <code>--fail-swap-on=false</code>。</p>
<p>虽说可以更改参数让其可用，但是我建议还是禁用 <code>swap</code> 除非你的集群有特殊的需求，比如：有大内存使用的需求，但又想节约成本；或者你知道你将要做什么，否则可能会出现一些非预期的情况，尤其是做了内存限制的时候，当某个 Pod 达到内存限制的时候，它可能会溢出到 swap 中，这会导致 K8S 无法正常进行调度。</p>
<p>如何禁用：</p>
<ol>
<li>使用 <code>sudo cat /proc/swaps</code> 验证 swap 配置的设备和文件。</li>
<li>通过 <code>swapoff -a</code> 关闭 swap 。</li>
<li>使用 <code>sudo blkid</code> 或者 <code>sudo lsblk</code> 可查看到我们的设备属性，请注意输出结果中带有 <code>swap</code> 字样的信息。</li>
<li>将 <code>/etc/fstab</code> 中和上一条命令中输出的，和 swap 相关的挂载点都删掉，以免在机器重启或重挂载时，再挂载 <code>swap</code> 分区。</li>
</ol>
<p>执行完上述操作，<code>swap</code> 便会被禁用，当然你也可以再次通过上述命令，或者 <code>free</code> 命令来确认是否还有 <code>swap</code> 存在。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="02706d6d76426f6371766770">[email&#160;protected]</a> ~]# free 
              total        used        free      shared  buff/cache   available
Mem:        1882748       85608     1614836       16808      182304     1630476
Swap:             0           0           0
</code></pre>
</li>
<li>
<p>通过 <code>sudo cat /sys/class/dmi/id/product_uuid</code> 可查看机器的 <code>product_uuid</code> 请确保要搭建集群的所有节点的 <code>product_uuid</code> 均不相同。同时所有节点的 Mac 地址也不能相同，通过 <code>ip a</code> 或者 <code>ifconfig -a</code> 可进行查看。</p>
<p>我们在第二章提到过，每个 Node 都有一些信息会被记录进集群内，而此处我们需要保证的这些唯一的信息，便会记录在集群的 <code>nodeInfo</code> 中，比如 <code>product_uuid</code> 在集群内以 <code>systemUUID</code> 来表示。具体信息我们可以通过集群的 <code>API Server</code> 获取到，在后面的章节会详细讲述。</p>
</li>
<li>
<p>第三章中，我们已经谈过 K8S 是 C/S 架构，在启动后，会固定监听一些端口用于提供服务。可以通过 <code>sudo netstat -ntlp |grep -E '6443|23[79,80]|1025[0,1,2]'</code> 查看这些端口是否被占用，如果被占用，请手动释放。</p>
<p>如果你执行上述命令时，提示 <code>command not found</code>，则表明你需要先安装 <code>netstat</code>，在 CentOS 系统中需要通过 <code>sudo yum install net-tools</code> 安装，而在 Debian/Ubuntu 系统中，则需要通过 <code>sudo apt install net-tools</code> 进行安装。</p>
</li>
<li>
<p>前面我们也提到了，我们需要一个容器运行时，通常情况下是 <code>Docker</code>，我们可以通过<a href="https://docs.docker.com/install/overview/">官方的 Docker 文档</a> 进行安装，安装完成后记得启动服务。</p>
<p>官方推荐使用 <code>17.03</code> ，但我建议你可以直接安装 <code>18.03</code> 或者更新的版本，因为 <code>17.03</code> 版本的 Docker 已经在 2018 年 3 月 <code>EOL</code>（End Of Life）了。对于更新版本的 Docker，虽然 K8S 尚未在新版本中经过大量测试，但毕竟新版本有很多 Bugfix 和新特性的增加，也能规避一些可能遇到的问题（比如个别情况下 container 不会自动删除的情况 (17.09) ）。</p>
<p>另外，由于 Docker 的 API 都是带有版本的，且有良好的兼容性，当使用低版本 API 请求时会自动降级，所以一般情况下也不会有什么问题。</p>
</li>
</ul>
<h3>安装 kubectl</h3>
<p>第三章中，我们已经说过 <code>kubectl</code> 是集群的客户端，我们现在搭建集群时，也必须要安装它，用于验证集群功能。</p>
<p>安装步骤在第 4 章已经详细说明了，此处不做赘述，可查阅第 4 章或参考下面的内容。</p>
<h3>安装 kubeadm 和 kubelet</h3>
<p>首先是版本的选择，我们可以通过下面的命令获取到当前的 stable 版本号。要访问这个地址，需要自行处理网络问题或使用我后面提供的解决办法。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="90e2ffffe4d0fdf1e3e4f5e2">[email&#160;protected]</a> ~]# curl -sSL https://dl.k8s.io/release/stable.txt
v1.11.3
</code></pre>
<p>下载二进制包，并通过 <code>kubeadm version</code> 验证版本是否正确。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="8af8e5e5fecae7ebf9feeff8">[email&#160;protected]</a> ~]# curl -sSL https://dl.k8s.io/release/v1.11.3/bin/linux/amd64/kubeadm &gt; /usr/bin/kubeadm
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="7f0d10100b3f121e0c0b1a0d">[email&#160;protected]</a> ~]# chmod a+rx /usr/bin/kubeadm
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="e4968b8b90a4898597908196">[email&#160;protected]</a> ~]# kubeadm version
kubeadm version: &amp;version.Info{Major:&quot;1&quot;, Minor:&quot;11&quot;, GitVersion:&quot;v1.11.3&quot;, GitCommit:&quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-09-09T17:59:42Z&quot;, GoVersion:&quot;go1.10.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
</code></pre>
<p>当然，我们其实可以使用如同上一章的方式，直接进入到 <code>kubernetes</code> 的<a href="https://github.com/kubernetes/kubernetes">官方仓库</a>，找到我们所需版本 <a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.11.md#v1113">v1.11.3</a> 下载 <code>Server Binaries</code>，如下图：</p>
<p><img src="assets/1660f7b43d86c139" alt="img" /></p>
<p>终端下可使用如下方式下载：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="e1938e8e95a18c8092958493">[email&#160;protected]</a> tmp]# wget -q https://dl.k8s.io/v1.11.3/kubernetes-server-linux-amd64.tar.gz
</code></pre>
<p><strong>对于国内用户，我已经准备了下面的方式，方便使用。</strong></p>
<pre><code>链接: https://pan.baidu.com/s/1FSEcEUplQQGsjyBIZ6j2fA 提取码: cu4s
</code></pre>
<p>下载完成后，验证文件是否正确无误，验证通过后进行解压。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ccbea3a3b88ca1adbfb8a9be">[email&#160;protected]</a> tmp]# echo 'e49d0db1791555d73add107d2110d54487df538b35b9dde0c5590ac4c5e9e039 kubernetes-server-linux-amd64.tar.gz' | sha256sum -c -
kubernetes-server-linux-amd64.tar.gz: 确定
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="40322f2f34002d2133342532">[email&#160;protected]</a> tmp]# tar -zxf kubernetes-server-linux-amd64.tar.gz
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="384a57574c7855594b4c5d4a">[email&#160;protected]</a> tmp]# ls kubernetes
addons  kubernetes-src.tar.gz  LICENSES  server
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="aedcc1c1daeec3cfdddacbdc">[email&#160;protected]</a> tmp]# ls kubernetes/server/bin/ | grep -E 'kubeadm|kubelet|kubectl'
kubeadm
kubectl
kubelet
</code></pre>
<p>可以看到在 <code>server/bin/</code> 目录下有我们所需要的全部内容，将我们所需要的 <code>kubeadm</code> <code>kubectl</code> <code>kubelet</code> 等都移动至 <code>/usr/bin</code> 目录下。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="addfc2c2d9edc0ccded9c8df">[email&#160;protected]</a> tmp]# mv kubernetes/server/bin/kube{adm,ctl,let} /usr/bin/
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b0c2dfdfc4f0ddd1c3c4d5c2">[email&#160;protected]</a> tmp]# ls /usr/bin/kube*
/usr/bin/kubeadm  /usr/bin/kubectl  /usr/bin/kubelet
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="b2c0ddddc6f2dfd3c1c6d7c0">[email&#160;protected]</a> tmp]# kubeadm version
kubeadm version: &amp;version.Info{Major:&quot;1&quot;, Minor:&quot;11&quot;, GitVersion:&quot;v1.11.3&quot;, GitCommit:&quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-09-09T17:59:42Z&quot;, GoVersion:&quot;go1.10.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="c5b7aaaab185a8a4b6b1a0b7">[email&#160;protected]</a> tmp]# kubectl version --client
Client Version: version.Info{Major:&quot;1&quot;, Minor:&quot;11&quot;, GitVersion:&quot;v1.11.3&quot;, GitCommit:&quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-09-09T18:02:47Z&quot;, GoVersion:&quot;go1.10.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="31435e5e45715c5042455443">[email&#160;protected]</a> tmp]# kubelet --version
Kubernetes v1.11.3
</code></pre>
<p>可以看到我们所需的组件，版本均为 <code>v1.11.3</code> 。</p>
<h2>配置</h2>
<p>为了在生产环境中保障各组件的稳定运行，同时也为了便于管理，我们增加对 <code>kubelet</code> 的 <code>systemd</code> 的配置，由 <code>systemd</code> 对服务进行管理。</p>
<h3>配置 kubelet</h3>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="e2908d8d96a28f8391968790">[email&#160;protected]</a> tmp]# cat &lt;&lt;'EOF' &gt; /etc/systemd/system/kubelet.service
[Unit]
Description=kubelet: The Kubernetes Agent
Documentation=http://kubernetes.io/docs/

[Service]
ExecStart=/usr/bin/kubelet
Restart=always
StartLimitInterval=0
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="bbc9d4d4cffbd6dac8cfdec9">[email&#160;protected]</a> tmp]# mkdir -p /etc/systemd/system/kubelet.service.d
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="fa8895958eba979b898e9f88">[email&#160;protected]</a> tmp]# cat &lt;&lt;'EOF' &gt; /etc/systemd/system/kubelet.service.d/kubeadm.conf
[Service]
Environment=&quot;KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf&quot;
Environment=&quot;KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml&quot;
EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
EnvironmentFile=-/etc/default/kubelet
ExecStart=
ExecStart=/usr/bin/kubelet $KUBELET_KUBECONFIG_ARGS $KUBELET_CONFIG_ARGS $KUBELET_KUBEADM_ARGS $KUBELET_EXTRA_ARGS
EOF
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="9ceef3f3e8dcf1fdefe8f9ee">[email&#160;protected]</a> tmp]# systemctl enable kubelet
Created symlink from /etc/systemd/system/multi-user.target.wants/kubelet.service to /etc/systemd/system/kubelet.service.
</code></pre>
<p>在这里我们添加了 <code>kubelet</code> 的 systemd 配置，然后添加了它的 <code>Drop-in</code> 文件，我们增加的这个 <code>kubeadm.conf</code> 文件，会被 systemd 自动解析，用于复写 <code>kubelet</code> 的基础 systemd 配置，可以看到我们增加了一系列的配置参数。在第 17 章中，我们会对 <code>kubelet</code> 做详细剖析，到时再进行解释。</p>
<h2>启动</h2>
<p>此时，我们的前期准备已经基本完成，可以使用 <code>kubeadm</code> 来创建集群了。别着急，在此之前，我们还需要安装两个工具，名为<code>crictl</code> 和 <code>socat</code>。</p>
<h3>安装前置依赖 crictl</h3>
<p><code>crictl</code> 包含在 <a href="https://github.com/kubernetes-sigs/cri-tools.git"><code>cri-tools</code></a> 项目中，这个项目中包含两个工具：</p>
<ul>
<li><code>crictl</code> 是 <code>kubelet</code> CRI (Container Runtime Interface) 的 CLI 。</li>
<li><code>critest</code> 是 <code>kubelet</code> CRI 的测试工具集。</li>
</ul>
<p>安装可以通过进入 <code>cri-tools</code> 项目的 <a href="https://github.com/kubernetes-sigs/cri-tools/releases">Release 页面</a> ，根据项目 <a href="https://github.com/kubernetes-sigs/cri-tools#current-status">README</a> 文件中的版本兼容关系，选择自己所需的安装包，下载即可，由于我们安装 K8S 1.11.3 所以选择最新的 v1.11.x 的安装包。</p>
<p><img src="assets/1660f7cee66145d1" alt="img" /></p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d7a5b8b8a397bab6a4a3b2a5">[email&#160;protected]</a> ~]# wget https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.11.1/crictl-v1.11.1-linux-amd64.tar.gz
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="82f0ededf6c2efe3f1f6e7f0">[email&#160;protected]</a> ~]# echo 'ccf83574556793ceb01717dc91c66b70f183c60c2bbec70283939aae8fdef768 crictl-v1.11.1-linux-amd64.tar.gz' | sha256sum -c -
crictl-v1.11.1-linux-amd64.tar.gz: 确定
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ddafb2b2a99db0bcaea9b8af">[email&#160;protected]</a> ~]# tar zxvf crictl-v1.11.1-linux-amd64.tar.gz
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="8ffde0e0fbcfe2eefcfbeafd">[email&#160;protected]</a> ~]# mv crictl /usr/bin/
</code></pre>
<h3>安装前置依赖 socat</h3>
<p><code>socat</code> 是一款很强大的命令行工具，可以建立两个双向字节流并在其中传输数据。这么说你也许不太理解，简单点说，它其中的一个功能是可以实现端口转发。</p>
<p>无论在 K8S 中，还是在 Docker 中，如果我们需要在外部访问服务，端口转发是个必不可少的部分。当然，你可能会问基本上没有任何地方提到说 <code>socat</code> 是一个依赖项啊，别急，我们来看下<a href="https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/dockershim/docker_streaming.go#L189-L192"> K8S 的源码</a>便知道了。</p>
<pre><code>func portForward(client libdocker.Interface, podSandboxID string, port int32, stream io.ReadWriteCloser) error {
    // 省略了和 socat 无关的代码

	socatPath, lookupErr := exec.LookPath(&quot;socat&quot;)
	if lookupErr != nil {
		return fmt.Errorf(&quot;unable to do port forwarding: socat not found.&quot;)
	}

	args := []string{&quot;-t&quot;, fmt.Sprintf(&quot;%d&quot;, containerPid), &quot;-n&quot;, socatPath, &quot;-&quot;, fmt.Sprintf(&quot;TCP4:localhost:%d&quot;, port)}

    // ...
}
</code></pre>
<p><code>socat</code> 的安装很简单 CentOS 下执行 <code>sudo yum install -y socat</code> ，Debian/Ubuntu 下执行 <code>sudo apt-get install -y socat</code> 即可完成安装。</p>
<h3>初始化集群</h3>
<p>所有的准备工作已经完成，我们开始真正创建一个 K8S 集群。 <strong>注意：如果需要配置 Pod 网络方案，请先阅读本章最后的部分 配置集群网络</strong></p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="74061b1b0034191507001106">[email&#160;protected]</a> ~]# kubeadm init                                                                                             
[init] using Kubernetes version: v1.11.3               
[preflight] running pre-flight checks
...
I0920 01:09:09.602908   17966 kernel_validator.go:81] Validating kernel version
I0920 01:09:09.603001   17966 kernel_validator.go:96] Validating kernel config
        [WARNING SystemVerification]: docker version is greater than the most recently validated version. Docker version: 18.03.1-ce. Max validated version: 17.03
[preflight/images] Pulling images required for setting up a Kubernetes cluster
[preflight/images] This might take a minute or two, depending on the speed of your internet connection
[preflight/images] You can also perform this action in beforehand using 'kubeadm config images pull'
[kubelet] Writing kubelet environment file with flags to file &quot;/var/lib/kubelet/kubeadm-flags.env&quot;
[kubelet] Writing kubelet configuration to file &quot;/var/lib/kubelet/config.yaml&quot;
[preflight] Activating the kubelet service
[certificates] Generated ca certificate and key.
[certificates] Generated apiserver certificate and key.
...
[markmaster] Marking the node master as master by adding the label &quot;node-role.kubernetes.io/master=''&quot;
[markmaster] Marking the node master as master by adding the taints [node-role.kubernetes.io/master:NoSchedule]
[bootstraptoken] creating the &quot;cluster-info&quot; ConfigMap in the &quot;kube-public&quot; namespace
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes master has initialized successfully!

...

You can now join any number of machines by running the following on each node
as root:

  kubeadm join 202.182.112.120:6443 --token t14kzc.vjurhx5k98dpzqdc --discovery-token-ca-cert-hash sha256:d64f7ce1af9f9c0c73d2d737fd0095456ad98a2816cb5527d55f984c8aa8a762
</code></pre>
<p>以上省略了部分输出。</p>
<p>我们从以上日志中可以看到，创建集群时会检查内核版本，Docker 版本等信息，这里提示 Docker 版本较高，我们忽略这个提示。</p>
<p>然后会下载一些镜像，当然这里提示我们可以通过执行 <code>kubeadm config images pull</code> 提前去下载镜像。我们来看下</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="80f2efeff4c0ede1f3f4e5f2">[email&#160;protected]</a> ~]# kubeadm config images pull
[config/images] Pulled k8s.gcr.io/kube-apiserver-amd64:v1.11.3
[config/images] Pulled k8s.gcr.io/kube-controller-manager-amd64:v1.11.3
[config/images] Pulled k8s.gcr.io/kube-scheduler-amd64:v1.11.3
[config/images] Pulled k8s.gcr.io/kube-proxy-amd64:v1.11.3
[config/images] Pulled k8s.gcr.io/pause:3.1
[config/images] Pulled k8s.gcr.io/etcd-amd64:3.2.18
[config/images] Pulled k8s.gcr.io/coredns:1.1.3
</code></pre>
<p>对于国内用户使用 <code>kubeadm</code> 创建集群时，可能遇到的问题便是这些镜像下载不下来，最终导致创建失败。所以我在国内的代码托管平台提供了一个<a href="https://gitee.com/K8S-release/kubeadm">仓库</a> 可以 clone 该项目，进入 <code>v1.11.3</code> 目录，对每个 <code>tar</code> 文件执行 <code>sudo docker load -i xx.tar</code> 即可将镜像导入。</p>
<p>或者可使用<a href="https://dev.aliyun.com/list.html?namePrefix=google-containers">阿里云提供的镜像</a>，只需要将 <code>k8s.gcr.io</code> 替换为 <code>registry.aliyuncs.com/google_containers</code> ，执行 <code>docker pull</code> 后再 <code>docker tag</code> 重 tag 即可。</p>
<p>继续看上面的日志，<code>kubeadm init</code> 执行起见生成了一些文件，而这些文件我们先前在 kubelet server 的 <code>Drop-in</code> 的配置中配置过。</p>
<p>生成这些配置文件后，将启动 <code>kubelet</code> 服务，生成一系列的证书和相关的配置之类的，并增加一些扩展。</p>
<p>最终集群创建成功，并提示可在任意机器上使用指定命令加入集群。</p>
<h2>验证</h2>
<p>在上面的步骤中，我们已经安装了 K8S 的 CLI 工具 <code>kubectl</code>，我们使用此工具查看集群信息：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="e5978a8a91a5888496918097">[email&#160;protected]</a> ~]# kubectl cluster-info
Kubernetes master is running at http://localhost:8080

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
The connection to the server localhost:8080 was refused - did you specify the right host or port?
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="82f0ededf6c2efe3f1f6e7f0">[email&#160;protected]</a> ~]# kubectl get nodes
The connection to the server localhost:8080 was refused - did you specify the right host or port?
</code></pre>
<p>使用 <code>kubectl cluster-info</code> 可查看集群 master 和集群服务的地址，但我们也注意到最后有一句报错 <code>connection ... refused</code> 很显然这里存在错误。</p>
<p><code>kubectl get nodes</code> 可查看集群中 <code>Node</code> 信息，同样报错。</p>
<p>在上面我们提到过，K8S 默认会监听一些端口，但并不是 <code>8080</code> 端口，由此可知，我们的 <code>kubectl</code> 配置有误。</p>
<h3>配置 kubectl</h3>
<ul>
<li>
<p>使用 <code>kubectl</code> 的参数 <code>--kubeconfig</code> 或者环境变量 <code>KUBECONFIG</code> 。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4e3c21213a0e232f3d3a2b3c">[email&#160;protected]</a> ~]# kubectl --kubeconfig /etc/kubernetes/admin.conf get nodes                                                
NAME      STATUS     ROLES     AGE       VERSION
master    NotReady   master    13h       v1.11.3
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1a6875756e5a777b696e7f68">[email&#160;protected]</a> ~]#
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="ec9e838398ac818d9f98899e">[email&#160;protected]</a> ~]# KUBECONFIG=/etc/kubernetes/admin.conf kubectl get nodes                                                  
NAME      STATUS     ROLES     AGE       VERSION
master    NotReady   master    13h       v1.11.3
</code></pre>
</li>
<li>
<p>使用传参的方式未免太繁琐，我们也可以更改默认配置文件</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="33415c5c47735e5240475641">[email&#160;protected]</a> ~]# mkdir -p $HOME/.kube
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1c6e7373685c717d6f68796e">[email&#160;protected]</a> ~]# sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="7c0e1313083c111d0f08190e">[email&#160;protected]</a> ~]# sudo chown $(id -u):$(id -g) $HOME/.kube/config
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="bdcfd2d2c9fdd0dccec9d8cf">[email&#160;protected]</a> ~]# kubectl get nodes                                                  
NAME      STATUS     ROLES     AGE       VERSION
master    NotReady   master    13h       v1.11.3
</code></pre>
</li>
</ul>
<h3>配置集群网络</h3>
<p>通过上面的配置，我们已经可以正常获取 <code>Node</code> 信息。但通过第 2 章，我们了解到 <code>Node</code> 都有 <code>status</code>，而此时我们唯一的 <code>Node</code> 是 <code>NotReady</code>。我们通过给 <code>kubectl</code> 传递 <code>-o</code> 参数更改输出格式，查看更详细的情况。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="9ceef3f3e8dcf1fdefe8f9ee">[email&#160;protected]</a> ~]# kubectl get nodes -o yaml
apiVersion: v1       
items:                                       
- apiVersion: v1                              
  kind: Node
  ...
  status:
    addresses:
    - address: master
      type: Hostname
    ...
    - lastHeartbeatTime: 2018-09-20T14:45:45Z
      lastTransitionTime: 2018-09-20T01:09:48Z
      message: 'runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady
        message:docker: network plugin is not ready: cni config uninitialized'
      reason: KubeletNotReady
      status: &quot;False&quot;
      type: Ready
    ...
</code></pre>
<p>从以上输出中，我们可以看到 master 处于 <code>NotReady</code> 的原因是 <code>network plugin is not ready: cni config uninitialized</code> 那么 <code>CNI</code> 是什么呢？<code>CNI</code> 是 Container Network Interface 的缩写，是 K8S 用于配置 Linux 容器网络的接口规范。</p>
<p>关于网络的选择，我们此处不做过多介绍，我们暂时选择一个被广泛使用的方案 <code>flannel</code>。 但注意，如果要使用 <code>flannel</code> 需要在 <code>kubeadm init</code> 的时候，传递 <code>--pod-network-cidr=10.244.0.0/16</code> 参数。另外需要查看 <code>/proc/sys/net/bridge/bridge-nf-call-iptables</code> 是否已设置为 <code>1</code>。 可以通过 <code>sysctl net.bridge.bridge-nf-call-iptables=1</code> 更改配置。</p>
<p>我们在前面创建集群时，并没有传递任何参数。为了能使用 <code>flannel</code> , 所以我们需要先将集群重置。使用 <code>kubeadm reset</code></p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="60120f0f14200d0113140512">[email&#160;protected]</a> ~]# kubeadm reset 
[reset] WARNING: changes made to this host by 'kubeadm init' or 'kubeadm join' will be reverted.
[reset] are you sure you want to proceed? [y/N]: y
[preflight] running pre-flight checks
[reset] stopping the kubelet service
[reset] unmounting mounted directories in &quot;/var/lib/kubelet&quot;
[reset] removing kubernetes-managed containers
[reset] cleaning up running containers using crictl with socket /var/run/dockershim.sock
[reset] failed to list running pods using crictl: exit status 1. Trying to use docker instead[reset] deleting contents of stateful directories: [/var/lib/kubelet /etc/cni/net.d /var/lib/dockershim /var/run/kubernetes /var/lib/etcd]
[reset] deleting contents of config directories: [/etc/kubernetes/manifests /etc/kubernetes/pki]
[reset] deleting files: [/etc/kubernetes/admin.conf /etc/kubernetes/kubelet.conf /etc/kubernetes/bootstrap-kubelet.conf /etc/kubernetes/controller-manager.conf /etc/kubernetes/scheduler.conf]
</code></pre>
<p>重新初始化集群，并传递参数。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="9eecf1f1eadef3ffedeafbec">[email&#160;protected]</a> ~]# kubeadm init --pod-network-cidr=10.244.0.0/16
[init] using Kubernetes version: v1.11.3
...
Your Kubernetes master has initialized successfully!
</code></pre>
<p><strong>注意：这里会重新生成相应证书等配置，需要按上面的内容重新配置 kubectl。</strong></p>
<p>此时，<code>CNI</code> 也尚未初始化完成，我们还需完成以下的步骤。</p>
<pre><code># 注意，这里的 flannel 配置仅适用于 1.11 版本的 K8S，若安装其他版本的 K8S 需要替换掉此链接
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="681a07071c2805091b1c0d1a">[email&#160;protected]</a> ~]# kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/v0.10.0/Documentation/kube-flannel.yml
clusterrole.rbac.authorization.k8s.io/flannel created
clusterrolebinding.rbac.authorization.k8s.io/flannel created
serviceaccount/flannel created
configmap/kube-flannel-cfg created
daemonset.extensions/kube-flannel-ds created
</code></pre>
<p>稍等片刻，再次查看 Node 状态：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="a1d3ceced5e1ccc0d2d5c4d3">[email&#160;protected]</a> ~]# kubectl get nodes
NAME      STATUS    ROLES     AGE       VERSION
master    Ready     master    12m       v1.11.3
</code></pre>
<p>可以看到 status 已经是 <code>Ready</code> 状态。根据第 3 章的内容，我们知道 K8S 中最小的调度单元是 <code>Pod</code> 我们来看下集群中现有 <code>Pod</code> 的状态。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d6a4b9b9a296bbb7a5a2b3a4">[email&#160;protected]</a> ~]# kubectl get pods --all-namespaces
NAMESPACE     NAME                             READY     STATUS              RESTARTS   AGE 
kube-system   coredns-78fcdf6894-h7pkc         0/1       ContainerCreating   0          12m
kube-system   coredns-78fcdf6894-lhlks         0/1       ContainerCreating   0          12m
kube-system   etcd-master                      1/1       Running             0          5m
kube-system   kube-apiserver-master            1/1       Running             0          5m
kube-system   kube-controller-manager-master   1/1       Running             0          5m
kube-system   kube-flannel-ds-tqvck            1/1       Running             0          6m
kube-system   kube-proxy-25tk2                 1/1       Running             0          12m
kube-system   kube-scheduler-master            1/1       Running             0          5m
</code></pre>
<p>我们发现有两个 <code>coredns</code> 的 <code>Pod</code> 是 <code>ContainerCreating</code> 的状态，但并未就绪。根据第 3 章的内容，我们知道 <code>Pod</code> 实际会有一个调度过程，此处我们暂且不论，后续章节再对此进行解释。</p>
<h3>新增 Node</h3>
<p>我们按照刚才执行完 <code>kubeadm init</code> 后，给出的信息，在新的机器上执行 <code>kubeadm join</code> 命令。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="1765787863577978737226">[email&#160;protected]</a> ~]# kubeadm join 202.182.112.120:6443 --token t14kzc.vjurhx5k98dpzqdc --discovery-token-ca-cert-hash sha256:d64f7ce1af9f9c0c73d2d737fd0095456ad98a2816cb5527d55f984c8aa8a762
[preflight] running pre-flight checks
        [WARNING RequiredIPVSKernelModulesAvailable]: the IPVS proxier will not be used, because the following required kernel modules are not loaded: [ip_vs ip_vs_rr ip_vs_wrr ip_vs_sh] or no builtin kernel ipvs support: map[ip_vs:{} ip_vs_rr:{} ip_vs_wrr:{} ip_vs_sh:{} nf_conntrack_ipv4:{}]
you can solve this problem with following methods:
 1. Run 'modprobe -- ' to load missing kernel modules;
2. Provide the missing builtin kernel ipvs support

I0921 04:00:54.805439   10677 kernel_validator.go:81] Validating kernel version                                                  
I0921 04:00:54.805604   10677 kernel_validator.go:96] Validating kernel config                                                   
        [WARNING SystemVerification]: docker version is greater than the most recently validated version. Docker version: 18.03.1-ce. Max validated version: 17.03
[discovery] Trying to connect to API Server &quot;202.182.112.120:6443&quot;
[discovery] Created cluster-info discovery client, requesting info from &quot;https://202.182.112.120:6443&quot;
[discovery] Requesting info from &quot;https://202.182.112.120:6443&quot; again to validate TLS against the pinned public key
[discovery] Cluster info signature and contents are valid and TLS certificate validates against pinned roots, will use API Server &quot;202.182.112.120:6443&quot;
[discovery] Successfully established connection with API Server &quot;202.182.112.120:6443&quot;
[kubelet] Downloading configuration for the kubelet from the &quot;kubelet-config-1.11&quot; ConfigMap in the kube-system namespace
[kubelet] Writing kubelet configuration to file &quot;/var/lib/kubelet/config.yaml&quot;
[kubelet] Writing kubelet environment file with flags to file &quot;/var/lib/kubelet/kubeadm-flags.env&quot;
[preflight] Activating the kubelet service
[tlsbootstrap] Waiting for the kubelet to perform the TLS Bootstrap...
[patchnode] Uploading the CRI Socket information &quot;/var/run/dockershim.sock&quot; to the Node API object &quot;node1&quot; as an annotation

This node has joined the cluster:
* Certificate signing request was sent to master and a response
  was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the master to see this node join the cluster.
</code></pre>
<p>上面的命令执行完成，提示已经成功加入集群。 此时，我们在 master 上查看下当前集群状态。</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="4e3c21213a0e232f3d3a2b3c">[email&#160;protected]</a> ~]# kubectl get nodes
NAME      STATUS    ROLES     AGE       VERSION
master    Ready     master    12m       v1.11.3
node1     Ready     &lt;none&gt;    7m        v1.11.3
</code></pre>
<p>可以看到 node1 已经加入了集群。</p>
<h2>总结</h2>
<p>在本节中，我们选择官方推荐的 <code>kubeadm</code> 工具在服务器上搭建了一套有两个节点的集群。</p>
<p><code>kubeadm</code> 可以自动的拉取相关组件的 Docker 镜像，并将其“组织”起来，免去了我们逐个部署相关组件的麻烦。</p>
<p>我们首先学习到了部署 K8S 时需要对系统做的基础配置，其次安装了一些必要的工具，以便 K8S 的功能可正常运行。</p>
<p>其次，我们学习到了 CNI 相关的知识，并在集群中部署了 <code>flannel</code> 网络方案。</p>
<p>最后，我们学习了增加 Node 的方法，以便后续扩展集群。</p>
<p>集群搭建方面的学习暂时告一段落，但这并不是结束，这才是真正的开始，从下一章开始，我们要学习集群管理相关的内容，学习如何真正使用 K8S 。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="04&#32;搭建&#32;Kubernetes&#32;集群&#32;-&#32;本地快速搭建.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="06&#32;集群管理：初识&#32;kubectl.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345d88e6270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Kubernetes%20%E4%BB%8E%E4%B8%8A%E6%89%8B%E5%88%B0%E5%AE%9E%E8%B7%B5/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
