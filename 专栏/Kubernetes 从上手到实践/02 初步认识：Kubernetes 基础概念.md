<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>02 初步认识：Kubernetes 基础概念.md</title>
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

                    <a class="current-tab" href="02&#32;初步认识：Kubernetes&#32;基础概念.md">02 初步认识：Kubernetes 基础概念.md</a>
                    

                </li>
                <li>

                    
                    <a href="03&#32;宏观认识：整体架构.md">03 宏观认识：整体架构.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;搭建&#32;Kubernetes&#32;集群&#32;-&#32;本地快速搭建.md">04 搭建 Kubernetes 集群 - 本地快速搭建.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;动手实践：搭建一个&#32;Kubernetes&#32;集群&#32;-&#32;生产可用.md">05 动手实践：搭建一个 Kubernetes 集群 - 生产可用.md</a>

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
                        <div><h1>02 初步认识：Kubernetes 基础概念</h1>
<p>好了，总算开始进入正题，抛弃掉死板的说教模式，我们以一个虚构的新成立的项目组为例开始我们的 Kubernetes 探索。(以下统一将 Kubernetes 简写为 K8S) 项目组目前就只有一个成员，我们称他为小张。项目组刚成立的时候，小张也没想好，具体要做什么，但肯定要对外提供服务的，所以先向公司申请了一台服务器。</p>
<h2>Node</h2>
<p>这台服务器可以用来做什么呢？跑服务，跑数据库，跑测试之类的都可以，我们将它所做的事情统称为工作(work) 那么，它便是工作节点 (worker Node) 对应于 K8S 中，这就是我们首先要认识的 Node 。</p>
<p>Node 可以是一台物理机，也可以是虚拟机，对于我们此处的项目来讲，这台服务器便是 K8S 中的 Node 。</p>
<h3>Node 状态</h3>
<p>当我们拿到这台服务器后，首先我们登录服务器查看下服务器的基本配置和信息。其实对于一个新加入 K8S 集群的 Node 也是一样，需要先检查它的状态，并将状态上报至集群的 master 。我们来看看服务器有哪些信息是我们所关心的。</p>
<h4>地址</h4>
<p>首先，我们所关心的是我们服务器的 IP 地址，包括内网 IP 和外网 IP。对应于 K8S 集群的话这个概念是类似的，内部 IP 可在 K8S 集群内访问，外部 IP 可在集群外访问。</p>
<p>其次，我们也会关心一下我们的主机名，比如在服务器上执行 <code>hostname</code> 命令，便可得到主机名。K8S 集群中，每个 Node 的主机名也会被记录下来。当然，我们可以通过给 Kubelet 传递一个 <code>--hostname-override</code> 的参数来覆盖默认的主机名。 (Kubelet 是什么，我们后面会解释)</p>
<h4>信息</h4>
<p>再之后，我们需要看下服务器的基本信息，比如看看系统版本信息， <code>cat /etc/issue</code> 或者 <code>cat /etc/os-release</code> 等方法均可查看。对于 K8S 集群会将每个 Node 的这些基础信息都记录下来。</p>
<h4>容量</h4>
<p>我们通常也都会关注下，我们有几个核心的 CPU ，可通过 <code>cat /proc/cpuinfo</code> 查看，有多大的内存 通过 <code>cat /proc/meminfo</code> 或 <code>free</code> 等查看。对于 K8S 集群，会默认统计这些信息，并计算在此 Node 上可调度的 Pod 数量。（Pod 后面做解释）</p>
<h4>条件</h4>
<p>对于我们拿到的服务器，我们关心上述的一些基本信息，并根据这些信息进行判断，这台机器是否能满足我们的需要。对 K8S 集群也同样，当判断上述信息均满足要求时候，便将集群内记录的该 Node 信息标记为 <code>Ready</code> （<code>Ready = True</code>），这样我们的服务器便正式的完成交付。我们来看下其他的部分。</p>
<h2>Deployment 和 Pod</h2>
<p>现在小张拿到的服务器已经是可用状态，虽然此时尚不知要具体做什么，但姑且先部署一个主页来宣布下项目组的成立。</p>
<p>我们来看下一般情况下的做法，先写一个静态页面，比如叫 index.html 然后在服务器上启动一个 Nginx 或者其他任何 Web 服务器，来提供对 index.html 的访问。</p>
<p>Nginx 的安装及配置可参考 <a href="https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/">Nginx 的官方文档</a>。最简单的配置大概类似下面这样（仅保留关键部分）：</p>
<pre><code>location / {
    root   /www;
    index  index.html;
}
</code></pre>
<p>对于 K8S 而言，我们想要的，能提供对 index.html 访问的服务便可理解为 Deployment 的概念，表明一种我们预期的目标状态。</p>
<p>而对于 Nginx 和 index.html 这个组合可以理解为其中的 Pod 概念，作为最小的调度单元。</p>
<h2>Container Runtime</h2>
<p>虽然此刻部署的内容只有官网，但是为了避免单点故障，于是小张又申请了两台服务器（虽然看起来可能是浪费了点），现在要对原有的服务进行扩容，其实在新的服务器上我们所做的事情也还保持原样，部署 Nginx，提供对 index.html 的访问，甚至配置文件都完全是一样的。可以看到在这种情况下，增加一台服务器，我们需要做一件完全重复的事情。</p>
<p>本着不浪费时间做重复的工作的想法，小张想，要不然用 <a href="https://www.ansible.com/">Ansible</a> 来统一管理服务器操作和配置吧，但考虑到后续服务器上还需要部署其他的服务，常规的这样部署，容易干扰彼此的环境。</p>
<p>所以我们想到了用虚拟化的技术，但是根据一般的经验，类似 <a href="https://www.linux-kvm.org/page/Main_Page">KVM</a> 这样的虚拟化技术，可能在资源消耗上较多, 不够轻量级。而容器化相对来看，比较轻量级，也比较符合我们的预期，一次构建，随处执行。我们选择当前最热门的 Docker .</p>
<p>既然技术选型确定了，那很简单，在我们现在三台服务器上安装 Docker ，安装过程不再赘述，可以参考 <a href="https://docs.docker.com/install/linux/docker-ce/centos/">Docker 的官方安装文档</a> 。</p>
<p>此时，我们需要做的事情，也便只是将我们的服务构建成一个镜像，需要编写一个 Dockerfile，构建一个镜像并部署到每台服务器上便可。</p>
<p>聊了这么多，我们现在已经将我们的服务运行到了容器中，而此处的 Docker 便是我们选择的容器运行时。选择它的最主要原因，便是为了环境隔离和避免重复工作。</p>
<p>而 Docker 如果对应于 K8S 集群中的概念，便是 Container Runtime，这里还有其他的选择，比如 rkt，runc 和其他实现了 OCI 规范的运行时。</p>
<h2>总结</h2>
<p>在这节里面，我们了解到了 Node 其实就是用于工作的服务器，它有一些状态和信息，当这些条件都满足一些条件判断时，Node 便处于 Ready 状态，可用于执行后续的工作。</p>
<p>Deployment 可理解为一种对期望状态的描述， Pod 作为集群中可调度的最小单元，我们会在后面详细讲解其细节。</p>
<p>Docker 是我们选择的容器运行时，可运行我们构建的服务镜像，减少在环境方面所做的重复工作，并且也非常便于部署。除了 Docker 外还存在其他的容器运行时。</p>
<p>了解到这些基本概念后，下节我们从宏观的角度上来认识 K8S 的整体架构，以便我们后续的学习和实践。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="01&#32;&#32;开篇：&#32;Kubernetes&#32;是什么以及为什么需要它.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="03&#32;宏观认识：整体架构.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345caff3670ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
