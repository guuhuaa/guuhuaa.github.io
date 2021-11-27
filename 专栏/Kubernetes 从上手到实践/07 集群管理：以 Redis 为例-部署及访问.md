<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>07 集群管理：以 Redis 为例-部署及访问.md</title>
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

                    <a class="current-tab" href="07&#32;集群管理：以&#32;Redis&#32;为例-部署及访问.md">07 集群管理：以 Redis 为例-部署及访问.md</a>
                    

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
                        <div><h1>07 集群管理：以 Redis 为例-部署及访问</h1>
<p>上节我们已经学习了 <code>kubectl</code> 的基础使用，本节我们使用 <code>kubectl</code> 在 K8S 中进行部署。</p>
<p><strong>前面我们已经说过，Pod 是 K8S 中最小的调度单元，所以我们无法直接在 K8S 中运行一个 container 但是我们可以运行一个 Pod 而这个 Pod 中只包含一个 container 。</strong></p>
<h2>从 <code>kubectl run</code> 开始</h2>
<p><code>kubectl run</code> 的基础用法如下：</p>
<pre><code>Usage:
  kubectl run NAME --image=image [--env=&quot;key=value&quot;] [--port=port] [--replicas=replicas] [--dry-run=bool] [--overrides=inline-json] [--command] -- [COMMAND] [args...] [options]
</code></pre>
<p><code>NAME</code> 和 <code>--image</code> 是必需项。分别代表此次部署的名字及所使用的镜像，其余部分之后进行解释。当然，在我们实际使用时，推荐编写配置文件并通过 <code>kubectl create</code> 进行部署。</p>
<h2>使用最小的 Redis 镜像</h2>
<p>在 Redis 的<a href="https://hub.docker.com/_/redis/">官方镜像列表</a>可以看到有很多的 tag 可供选择，其中使用 <a href="https://alpinelinux.org/">Alpine Linux</a> 作为基础的镜像体积最小，下载较为方便。我们选择 <code>redis:alpine</code> 这个镜像进行部署。</p>
<h2>部署</h2>
<p>现在我们只部署一个 Redis 实例。</p>
<pre><code>➜  ~ kubectl run redis --image='redis:alpine'
deployment.apps/redis created
</code></pre>
<p>可以看到提示 <code>deployment.apps/redis created</code> 这个稍后进行解释，我们使用 <code>kubectl get all</code> 来看看到底发生了什么。</p>
<pre><code>➜  ~ kubectl get all
NAME                         READY     STATUS    RESTARTS   AGE
pod/redis-7c7545cbcb-2m6rp   1/1       Running   0          30s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    &lt;none&gt;        443/TCP   32s

NAME                    DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/redis   1         1         1            1           30s

NAME                               DESIRED   CURRENT   READY     AGE
replicaset.apps/redis-7c7545cbcb   1         1         1         30s
</code></pre>
<p>可以看到其中有我们刚才执行 <code>run</code> 操作后创建的 <code>deployment.apps/redis</code>，还有 <code>replicaset.apps/redis-7c7545cbcb</code>, <code>service/kubernetes</code> 以及 <code>pod/redis-7c7545cbcb-f984p</code>。</p>
<p>使用 <code>kubectl get all</code> 输出内容的格式 <code>/</code> 前代表类型，<code>/</code> 后是名称。</p>
<p>这些分别代表什么含义？</p>
<h3>Deployment</h3>
<p><code>Deployment</code> 是一种高级别的抽象，允许我们进行扩容，滚动更新及降级等操作。我们使用 <code>kubectl run redis --image='redis:alpine</code> 命令便创建了一个名为 <code>redis</code> 的 <code>Deployment</code>，并指定了其使用的镜像为 <code>redis:alpine</code>。</p>
<p>同时 K8S 会默认为其增加一些标签（<code>Label</code>）。我们可以通过更改 <code>get</code> 的输出格式进行查看。</p>
<pre><code>➜  ~ kubectl get deployment.apps/redis -o wide 
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE       CONTAINERS   IMAGES         SELECTOR
redis     1         1         1            1           40s       redis        redis:alpine   run=redis
➜  ~ kubectl get deploy redis -o wide          
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE       CONTAINERS   IMAGES         SELECTOR
redis     1         1         1            1           40s       redis        redis:alpine   run=redis
</code></pre>
<p>那么这些 <code>Label</code> 有什么作用呢？它们可作为选择条件进行使用。如：</p>
<pre><code>➜  ~ kubectl get deploy -l run=redis -o wide 
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE       CONTAINERS   IMAGES         SELECTOR
redis     1         1         1            1           11h       redis        redis:alpine   run=redis
➜  ~ kubectl get deploy -l run=test -o wide  # 由于我们并没有创建过 test 所以查不到任何东西
No resources found.
</code></pre>
<p>我们在应用部署或更新时总是会考虑的一个问题是如何平滑升级，利用 <code>Deployment</code> 也能很方便的进行金丝雀发布（Canary deployments）。这主要也依赖 <code>Label</code> 和 <code>Selector</code>， 后面我们再详细介绍如何实现。</p>
<p><code>Deployment</code> 的创建除了使用我们这里提到的方式外，更推荐的方式便是使用 <code>yaml</code> 格式的配置文件。在配置文件中主要是声明一种预期的状态，而其他组件则负责协同调度并最终达成这种预期的状态。当然这也是它的关键作用之一，将 <code>Pod</code> 托管给下面将要介绍的 <code>ReplicaSet</code>。</p>
<h3>ReplicaSet</h3>
<p><code>ReplicaSet</code> 是一种较低级别的结构，允许进行扩容。</p>
<p>我们上面已经提到 <code>Deployment</code> 主要是声明一种预期的状态，并且会将 <code>Pod</code> 托管给 <code>ReplicaSet</code>，而 <code>ReplicaSet</code> 则会去检查当前的 <code>Pod</code> 数量及状态是否符合预期，并尽量满足这一预期。</p>
<p><code>ReplicaSet</code> 可以由我们自行创建，但一般情况下不推荐这样去做，因为如果这样做了，那其实就相当于跳过了 <code>Deployment</code> 的部分，<code>Deployment</code> 所带来的功能或者特性我们便都使用不到了。</p>
<p>除了 <code>ReplicaSet</code> 外，我们还有一个选择名为 <code>ReplicationController</code>，这两者的主要区别更多的在选择器上，我们后面再做讨论。现在推荐的做法是 <code>ReplicaSet</code> 所以不做太多解释。</p>
<p><code>ReplicaSet</code> 可简写为 <code>rs</code>，通过以下命令查看：</p>
<pre><code>➜  ~ kubectl get rs -o wide
NAME               DESIRED   CURRENT   READY     AGE       CONTAINERS   IMAGES         SELECTOR                           
redis-7c7545cbcb   1         1         1         11h       redis        redis:alpine   pod-template-hash=3731017676,run=redis
</code></pre>
<p>在输出结果中，我们注意到这里除了我们前面看到的 <code>run=redis</code> 标签外，还多了一个 <code>pod-template-hash=3731017676</code> 标签，这个标签是由 <code>Deployment controller</code> 自动添加的，目的是为了防止出现重复，所以将 <code>pod-template</code> 进行 hash 用作唯一性标识。</p>
<h3>Service</h3>
<p><code>Service</code> 简单点说就是为了能有个稳定的入口访问我们的应用服务或者是一组 <code>Pod</code>。通过 <code>Service</code> 可以很方便的实现服务发现和负载均衡。</p>
<pre><code>➜  ~ kubectl get service -o wide
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE       SELECTOR
kubernetes   ClusterIP   10.96.0.1    &lt;none&gt;        443/TCP   16m        &lt;none&gt;
</code></pre>
<p>通过使用 <code>kubectl</code> 查看，能看到主要会显示 <code>Service</code> 的名称，类型，IP，端口及创建时间和选择器等。我们来具体拆解下。</p>
<h4>类型</h4>
<p><code>Service</code> 目前有 4 种类型：</p>
<ul>
<li><code>ClusterIP</code>： 是 K8S 当前默认的 <code>Service</code> 类型。将 service 暴露于一个仅集群内可访问的虚拟 IP 上。</li>
<li><code>NodePort</code>： 是通过在集群内所有 <code>Node</code> 上都绑定固定端口的方式将服务暴露出来，这样便可以通过 <code>&lt;NodeIP&gt;:&lt;NodePort&gt;</code> 访问服务了。</li>
<li><code>LoadBalancer</code>： 是通过 <code>Cloud Provider</code> 创建一个外部的负载均衡器，将服务暴露出来，并且会自动创建外部负载均衡器路由请求所需的 <code>Nodeport</code> 或 <code>ClusterIP</code> 。</li>
<li><code>ExternalName</code>： 是通过将服务由 DNS CNAME 的方式转发到指定的域名上将服务暴露出来，这需要 <code>kube-dns</code> 1.7 或更高版本支持。</li>
</ul>
<h4>实践</h4>
<p>上面已经说完了 <code>Service</code> 的基本类型，而我们也已经部署了一个 Redis ,当还无法访问到该服务，接下来我们将刚才部署的 Redis 服务暴露出来。</p>
<pre><code>➜  ~ kubectl expose deploy/redis --port=6379 --protocol=TCP --target-port=6379 --name=redis-server  
service/redis-server exposed
➜  ~ kubectl get svc -o wide                                                                       
NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE       SELECTOR
kubernetes     ClusterIP   10.96.0.1       &lt;none&gt;        443/TCP    49m       &lt;none&gt;
redis-server   ClusterIP   10.108.105.63   &lt;none&gt;        6379/TCP   4s        run=redis
</code></pre>
<p>通过 <code>kubectl expose</code> 命令将 redis server 暴露出来，这里需要进行下说明：</p>
<ul>
<li><code>port</code>： 是 <code>Service</code> 暴露出来的端口，可通过此端口访问 <code>Service</code>。</li>
<li><code>protocol</code>： 是所用协议。当前 K8S 支持 TCP/UDP 协议，在 1.12 版本中实验性的加入了对 <a href="https://zh.wikipedia.org/zh-hans/流控制传输协议">SCTP 协议</a>的支持。默认是 TCP 协议。</li>
<li><code>target-port</code>： 是实际服务所在的目标端口，请求由 <code>port</code> 进入通过上述指定 <code>protocol</code> 最终流向这里配置的端口。</li>
<li><code>name</code>： <code>Service</code> 的名字，它的用处主要在 dns 方面。</li>
<li><code>type</code>： 是前面提到的类型，如果没指定默认是 <code>ClusterIP</code>。</li>
</ul>
<p>现在我们的 redis 是使用的默认类型 <code>ClusterIP</code>，所以并不能直接通过外部进行访问，我们使用 <code>port-forward</code> 的方式让它可在集群外部访问。</p>
<pre><code>➜  ~ kubectl port-forward svc/redis-server 6379:6379
Forwarding from 127.0.0.1:6379 -&gt; 6379
Forwarding from [::1]:6379 -&gt; 6379
Handling connection for 6379
</code></pre>
<p>在另一个本地终端内可通过 redis-cli 工具进行连接：</p>
<pre><code>➜  ~ redis-cli -h 127.0.0.1 -p 6379
127.0.0.1:6379&gt; ping
PONG
</code></pre>
<p>当然，我们也可以使用 <code>NodePort</code> 的方式对外暴露服务。</p>
<pre><code>➜  ~ kubectl expose deploy/redis --port=6379 --protocol=TCP --target-port=6379 --name=redis-server-nodeport --type=NodePort
service/redis-server-nodeport exposed
➜  ~ kubectl get service/redis-server-nodeport -o wide 
NAME                    TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE       SELECTOR
redis-server-nodeport   NodePort   10.109.248.204   &lt;none&gt;        6379:31913/TCP   11s       run=redis
</code></pre>
<p>我们可以通过任意 <code>Node</code> 上的 31913 端口便可连接我们的 redis 服务。当然，这里需要注意的是这个端口范围其实是可以通过 <code>kube-apiserver</code> 的 <code>service-node-port-range</code> 进行配置的，默认是 <code>30000-32767</code>。</p>
<h3>Pod</h3>
<p>第二节中，我们提到过 <code>Pod</code> 是 K8S 中的最小化部署单元。我们看下当前集群中 <code>Pod</code> 的状态。</p>
<pre><code>➜  ~ kubectl get pods
NAME                     READY     STATUS    RESTARTS   AGE
redis-7c7545cbcb-jwcf2   1/1       Running   0          8h
</code></pre>
<p>我们进行一次简单的扩容操作。</p>
<pre><code>➜  ~ kubectl scale deploy/redis --replicas=2
deployment.extensions/redis scaled
➜  ~ kubectl get pods
NAME                     READY     STATUS    RESTARTS   AGE
redis-7c7545cbcb-jwcf2   1/1       Running   0          8h
redis-7c7545cbcb-wzh6w   1/1       Running   0          4s
</code></pre>
<p>可以看到 <code>Pod</code> 数已经增加，并且也已经是 <code>Running</code> 的状态了。(当然在生产环境中 Redis 服务的扩容并不是使用这种方式进行扩容的，需要看实际的部署方式以及业务的使用姿势。)</p>
<h2>总结</h2>
<p>本节我们使用 Redis 作为例子，学习了集群管理相关的基础知识。学习了如何进行应用部署， <code>Service</code> 的基础类型以及如何通过 <code>port-forward</code> 或 <code>NodePort</code> 等方式将服务提供至集群的外部访问。</p>
<p>同时我们学习了应用部署中主要会涉及到的几类资源 <code>Deployment</code>，<code>Replicaset</code>，<code>Service</code> 和 <code>Pod</code> 等。对这些资源及它们之间关系的掌握，对于后续集群维护或定位问题有很大的帮助。</p>
<p>下节，我们开始学习在生产环境中使用 K8S 至关重要的一环，权限控制。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="06&#32;集群管理：初识&#32;kubectl.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="08&#32;安全重点&#32;认证和授权.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345e3d9bb70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
