<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>18  庖丁解牛：Container Runtime （Docker）.md</title>
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

                    <a class="current-tab" href="18&#32;&#32;庖丁解牛：Container&#32;Runtime&#32;（Docker）.md">18  庖丁解牛：Container Runtime （Docker）.md</a>
                    

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
                        <div><h1>18  庖丁解牛：Container Runtime （Docker）</h1>
<h2>整体概览</h2>
<p>我们在第 3 节的时候，提到过 <code>Container Runtime</code> 的概念，也大致介绍过它的主要作用在于下载镜像，运行容器等。</p>
<p>经过我们前面的学习，<code>kube-scheduler</code> 决定了 <code>Pod</code> 将被调度到哪个 <code>Node</code> 上，而 <code>kubelet</code> 则负责 <code>Pod</code> 在此 <code>Node</code> 上可按预期工作。如果没有 <code>Container Runtime</code>，那 <code>Pod</code> 中的 <code>container</code> 在该 <code>Node</code> 上也便无法正常启动运行了。</p>
<p>本节中，我们以当前最为通用的 <code>Container Runtime</code> Docker 为例进行介绍。</p>
<h2>Container Runtime 是什么</h2>
<p><code>Container Runtime</code> 我们通常叫它容器运行时，而这一概念的产生也是由于容器化技术和 K8S 的大力发展，为了统一工业标准，也为了避免 K8S 绑定于特定的容器运行时，所以便成立了 <a href="https://www.opencontainers.org/">Open Container Initiative (OCI)</a> 组织，致力于将容器运行时标准化和容器镜像标准化。</p>
<p>凡是遵守此标准的实现，均可由标准格式的镜像启动相应的容器，并完成一些特定的操作。</p>
<h2>Docker 是什么</h2>
<p>Docker 是一个容器管理平台，它最初是被设计用于快速创建，发布和运行容器的工具，不过随着它的发展，其中集成了越来越多的功能。</p>
<p>Docker 也可以说是一个包含标准容器运行时的工具集，当前版本中默认的 <code>runtime</code> 称之为 <code>runc</code>。 关于 <code>runc</code> 相关的一些内容可参考<a href="http://moelove.info/2018/11/23/runc-1.0-rc6-发布之际/">我之前的一篇文章</a>。</p>
<p>当然，这里提到了 <strong>默认的运行时</strong> 那也就意味着它可支持其他的运行时实现。</p>
<h2>CRI 是什么</h2>
<p>说到这里，我们就会发现，K8S 作为目前云原生技术体系中最重要的一环，为了让它更有扩展性，当然也不会将自己完全局限于某一种特定的容器运行时。</p>
<p>自 K8S 1.5 （2016 年 11 月）开始，新增了一个容器运行时的插件 API，并称之为 <code>CRI</code> （Container Runtime Interface），通过 <code>CRI</code> 可以支持 <code>kubelet</code> 使用不同的容器运行时，而不需要重新编译。</p>
<p><code>CRI</code> 主要是基于 gRPC 实现了 <code>RuntimeService</code> 和 <code>ImageService</code> 这两个服务，可以参考 <code>pkg/kubelet/apis/cri/runtime/v1alpha2/api.proto</code> 中的 API 定义。由于本节侧重于 <code>Container Runtime/Docker</code> 这里就不对 <code>CRI</code> 的具体实现进行展开了。</p>
<p>只要继续将 <code>kubelet</code> 当作 agent 的角色，而它与基于 <code>CRI</code> 实现的 <code>CRI shim</code> 服务进行通信理解即可。</p>
<h2>Docker 如何工作</h2>
<p>这里我们主要介绍在 K8S 中一些 Docker 常见的动作。</p>
<h3>部署一个 Redis</h3>
<pre><code>master $ kubectl run redis --image=redis
deployment.apps/redis created
master $ kubectl get all
NAME                        READY     STATUS              RESTARTS   AGE
pod/redis-bb7894d65-7vsj8   0/1       ContainerCreating   0          6s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    &lt;none&gt;        443/TCP   26m

NAME                    DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/redis   1         1         1            0           6s

NAME                              DESIRED   CURRENT   READY     AGE
replicaset.apps/redis-bb7894d65   1         1         0         6s
</code></pre>
<p>我们直接使用 <code>kubectl run</code> 的方式部署了一个 Redis</p>
<h3>查看详情</h3>
<pre><code>master $ kubectl describe pod/redis-bb7894d65-7vsj8
Name:               redis-bb7894d65-7vsj8
Namespace:          default
Priority:           0
PriorityClassName:  &lt;none&gt;
Node:               node01/172.17.0.21
Start Time:         Sat, 15 Dec 2018 04:48:49 +0000
Labels:             pod-template-hash=663450821
                    run=redis
Annotations:        &lt;none&gt;
Status:             Running
IP:                 10.40.0.1
Controlled By:      ReplicaSet/redis-bb7894d65
Containers:
  redis:
    Container ID:   docker://ab87085456aca76825dd639bcde27160d9c2c84cac5388585bcc9ed3afda6522
    Image:          redis
    Image ID:       docker-pullable://<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="cfbdaaaba6bc8fbca7aefdfaf9">[email&#160;protected]</a>:010a8bd5c6a9d469441aa35187d18c181e3195368bce309348b3ee639fce96e0
    Port:           &lt;none&gt;
    Host Port:      &lt;none&gt;
    State:          Running
      Started:      Sat, 15 Dec 2018 04:48:57 +0000
    Ready:          True
    Restart Count:  0
    Environment:    &lt;none&gt;
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-zxt27 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  default-token-zxt27:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-zxt27
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  &lt;none&gt;
Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  7m    default-scheduler  Successfully assigned default/redis-bb7894d65-7vsj8to node01
  Normal  Pulling    7m    kubelet, node01    pulling image &quot;redis&quot;
  Normal  Pulled     7m    kubelet, node01    Successfully pulled image &quot;redis&quot;
  Normal  Created    7m    kubelet, node01    Created container
  Normal  Started    7m    kubelet, node01    Started container
</code></pre>
<p>可以通过 <code>kubectl describe</code> 查看该 <code>Pod</code> 的事件详情。这里主要有几个阶段。</p>
<h4>调度</h4>
<pre><code>Normal  Scheduled  7m    default-scheduler  Successfully assigned default/redis-bb7894d65-7vsj8to node01
</code></pre>
<p>在第 15 小节 <code>kube-scheduler</code> 中我们介绍过，通过 <code>kube-scheduler</code> 可以决定 <code>Pod</code> 会调度到哪个 <code>Node</code>。本例中，<code>redis-bb7894d65-7vsj8to</code> 被调度到了 <code>node01</code>。</p>
<h4>pull 镜像</h4>
<pre><code>Normal  Pulling    7m    kubelet, node01    pulling image &quot;redis&quot;
Normal  Pulled     7m    kubelet, node01    Successfully pulled image &quot;redis&quot;
</code></pre>
<p>这里 <code>kubelet</code> 及该节点上的 <code>Container Runtime</code> （Docker）开始发挥作用，先拉取镜像。如果此刻你登录 <code>node01</code> 的机器，执行 <code>docker pull redis</code> 便可同步看到拉取进度。</p>
<h4>创建镜像并启动</h4>
<pre><code>Normal  Created    7m    kubelet, node01    Created container
Normal  Started    7m    kubelet, node01    Started container
</code></pre>
<p>拉取镜像完成后，便会开始创建并启动该容器，并返回任务结果。此刻登录 <code>node01</code> 机器，便会看到当前在运行的容器了。</p>
<pre><code>node01 $ docker ps |grep redis
ab87085456ac        <a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="a8dacdccc1dbe8dbc0c99a9d9e">[email&#160;protected]</a>:010a8bd5c6a9d469441aa35187d18c181e3195368bce309348b3ee639fce96e0  &quot;docker-entrypoint...&quot;   19 minutes ago      Up 19 minutes                           k8s_redis_redis-bb7894d65-7vsj8_default_b693b56c-0024-11e9-9bab-0242ac11000a_0
8f264abd82fe        k8s.gcr.io/pause:3.1  &quot;/pause&quot;                 19 minutes ago      Up 19 minutes                           k8s_POD_redis-bb7894d65-7vsj8_default_b693b56c-0024-11e9-9bab-0242ac11000a_0
</code></pre>
<h2>总结</h2>
<p>本节我们介绍了 <code>Container Runtime</code> 的基本概念，及 K8S 为了能增加扩展性，提供了统一的 <code>CRI</code> 插件接口，可用于支持多种容器运行时。</p>
<p>当前使用最为广泛的是 <a href="https://github.com/moby/moby/"><code>Docker</code></a>，当前还支持的主要有 <a href="https://github.com/opencontainers/runc"><code>runc</code></a>，<a href="https://github.com/containerd/containerd"><code>Containerd</code></a>，<a href="https://github.com/hyperhq/runv"><code>runV</code></a> 以及 <a href="https://github.com/rkt/rkt"><code>rkt</code></a> 等。</p>
<p>由于 Docker 的知识点很多，关于 Docker 的实践和内部原理可参考我之前的一次分享 <a href="https://github.com/tao12345666333/slides/raw/master/2018.09.13-Tech-Talk-Time/Docker实战和基本原理-张晋涛.pdf">Docker 实战和基本原理</a>。</p>
<p>在使用 K8S 时，也有极个别情况需要通过排查 Docker 的日志来分析问题。</p>
<p>至此，K8S 中主要的核心组件我们已经介绍完毕，下节我们主要集中于在 K8S 环境中，如何定位和解决问题，以及类似刚才提到的需要通过 Docker 进行排查问题的情况。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="17&#32;庖丁解牛：kube-proxy.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="19&#32;Troubleshoot.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43461a9d6870ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
