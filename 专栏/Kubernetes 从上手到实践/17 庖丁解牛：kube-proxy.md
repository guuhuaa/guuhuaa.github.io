<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>17 庖丁解牛：kube-proxy.md</title>
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

                    <a class="current-tab" href="17&#32;庖丁解牛：kube-proxy.md">17 庖丁解牛：kube-proxy.md</a>
                    

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
                        <div><h1>17 庖丁解牛：kube-proxy</h1>
<h2>整体概览</h2>
<p>在第 3 节中，我们了解到 <code>kube-proxy</code> 的存在，而在第 7 中，我们学习到了如何将运行于 K8S 中的服务以 <code>Service</code> 的方式暴露出来，以供访问。</p>
<p>本节，我们来介绍下 <code>kube-proxy</code> 了解下它是如何支撑起这种类似服务发现和代理相关功能的。</p>
<h2><code>kube-proxy</code> 是什么</h2>
<p><code>kube-proxy</code> 是 K8S 运行于每个 <code>Node</code> 上的网络代理组件，提供了 TCP 和 UDP 的连接转发支持。</p>
<p>我们已经知道，当 <code>Pod</code> 在创建和销毁的过程中，IP 可能会发生变化，而这就容易造成对其有依赖的服务的异常，所以通常情况下，我们都会使用 <code>Service</code> 将后端 <code>Pod</code> 暴露出来，而 <code>Service</code> 则较为稳定。</p>
<p>还是以我们之前的 <a href="https://github.com/tao12345666333/saythx"><code>SayThx</code></a> 项目为例，但我们只部署其中没有任何依赖的后端资源 <code>Redis</code> 。</p>
<pre><code>master $ git clone https://github.com/tao12345666333/saythx.git
Cloning into 'saythx'...
remote: Enumerating objects: 110, done.
remote: Counting objects: 100% (110/110), done.
remote: Compressing objects: 100% (82/82), done.
remote: Total 110 (delta 27), reused 102 (delta 20), pack-reused 0
Receiving objects: 100% (110/110), 119.42 KiB | 0 bytes/s, done.
Resolving deltas: 100% (27/27), done.
Checking connectivity... done.
master $ cd saythx/deploy
master $ ls
backend-deployment.yaml  frontend-deployment.yaml  namespace.yaml         redis-service.yaml
backend-service.yaml     frontend-service.yaml     redis-deployment.yaml  work-deployment.yaml
</code></pre>
<p>进入配置文件所在目录后，开始创建相关资源：</p>
<pre><code>master $ kubectl apply -f namespace.yaml
namespace/work created
master $ kubectl apply -f redis-deployment.yaml
deployment.apps/saythx-redis created
master $ kubectl  apply -f redis-service.yaml
service/saythx-redis created
master $ kubectl -n work get all
NAME                               READY     STATUS    RESTARTS   AGE
pod/saythx-redis-8558c7d7d-wsn2w   1/1       Running   0          21s

NAME                   TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/saythx-redis   NodePort   10.103.193.175   &lt;none&gt;        6379:31269/TCP   6s

NAME                           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/saythx-redis   1         1         1            1           21s

NAME                                     DESIRED   CURRENT   READY     AGE
replicaset.apps/saythx-redis-8558c7d7d   1         1         1         21s
</code></pre>
<p>可以看到 Redis 正在运行，并通过 <code>NodePort</code> 类型的 <code>Service</code> 暴露出来，我们访问来确认下。</p>
<pre><code>master $ docker run --rm -it --network host redis:alpine redis-cli -p 31269
Unable to find image 'redis:alpine' locally
alpine: Pulling from library/redis
4fe2ade4980c: Already exists
fb758dc2e038: Pull complete
989f7b0c858b: Pull complete
8dd99d530347: Pull complete
7137334fa8f0: Pull complete
30610ca64487: Pull complete
Digest: sha256:8fd83c5986f444f1a5521e3eda7395f0f21ff16d33cc3b89d19ca7c58293c5dd
Status: Downloaded newer image for redis:alpine
127.0.0.1:31269&gt; set name kubernetes
OK
127.0.0.1:31269&gt; get name 
&quot;kubernetes&quot;
</code></pre>
<p>可以看到已经可以正常访问。接下来，我们来看下 <code>31269</code> 这个端口的状态。</p>
<pre><code>master $ netstat  -ntlp |grep 31269
tcp6       0      0 :::31269                :::*                    LISTEN      2716/kube-proxy
</code></pre>
<p>可以看到该端口是由 <code>kube-proxy</code> 所占用的。</p>
<p>接下来，查看当前集群的 <code>Service</code> 和 <code>Endpoint</code></p>
<pre><code>master $ kubectl -n work get svc
NAME           TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
saythx-redis   NodePort   10.103.193.175   &lt;none&gt;        6379:31269/TCP   10m
master $ kubectl -n work get endpoints
NAME           ENDPOINTS        AGE
saythx-redis   10.32.0.2:6379   10m
master $ kubectl -n work get pod -o wide
NAME                           READY     STATUS    RESTARTS   AGE       IP          NODE      NOMINATED NODE
saythx-redis-8558c7d7d-wsn2w   1/1       Running   0          12m       10.32.0.2   node01    &lt;none&gt;
</code></pre>
<p>可以很直观的看到 <code>Endpoint</code> 当中的便是 <code>Pod</code> 的 IP，现在我们将该服务进行扩容（实际情况下并不会这样处理）。</p>
<p>直接通过 <code>kubectl scale</code> 操作</p>
<pre><code>master $ kubectl  -n work scale --replicas=2 deploy/saythx-redis
deployment.extensions/saythx-redis scaled
master $ kubectl  -n work get all
NAME                               READY     STATUS    RESTARTS   AGE
pod/saythx-redis-8558c7d7d-sslpj   1/1       Running   0          10s
pod/saythx-redis-8558c7d7d-wsn2w   1/1       Running   0          16m

NAME                   TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/saythx-redis   NodePort   10.103.193.175   &lt;none&gt;        6379:31269/TCP   16m

NAME                           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/saythx-redis   2         2         2            2           16m
</code></pre>
<p>查看 <code>Endpoint</code> 信息：</p>
<pre><code>master $ kubectl -n work get endpoints
NAME           ENDPOINTS                       AGE
saythx-redis   10.32.0.2:6379,10.32.0.3:6379   17m
</code></pre>
<p>可以看到 <code>Endpoint</code> 已经自动发生了变化，而这也意味着 <code>Service</code> 代理的后端节点将增加一个。</p>
<h2><code>kube-proxy</code> 如何工作</h2>
<p><code>kube-proxy</code> 在 Linux 系统上当前支持三种模式，可通过 <code>--proxy-mode</code> 配置：</p>
<ul>
<li><code>userspace</code>：这是很早期的一种方案，但效率上显著不足，不推荐使用。</li>
<li><code>iptables</code>：当前的默认模式。比 <code>userspace</code> 要快，但问题是会给机器上产生很多 <code>iptables</code> 规则。</li>
<li><code>ipvs</code>：为了解决 <code>iptables</code> 的性能问题而引入，采用增量的方式进行更新。</li>
</ul>
<p>下面我们以 <code>iptables</code> 的模式稍作介绍。</p>
<pre><code>master $ iptables -t nat -L 
Chain PREROUTING (policy ACCEPT)
target     prot opt source               destination
KUBE-SERVICES  all  --  anywhere             anywhere             /* kubernetes service portals */
DOCKER     all  --  anywhere             anywhere             ADDRTYPE match dst-type LOCAL

Chain INPUT (policy ACCEPT)
target     prot opt source               destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
KUBE-SERVICES  all  --  anywhere             anywhere             /* kubernetes service portals */
DOCKER     all  --  anywhere            !127.0.0.0/8          ADDRTYPE match dst-type LOCAL

Chain POSTROUTING (policy ACCEPT)
target     prot opt source               destination
KUBE-POSTROUTING  all  --  anywhere             anywhere             /* kubernetes postrouting rules */
MASQUERADE  all  --  172.18.0.0/24        anywhere

Chain DOCKER (2 references)
target     prot opt source               destination
RETURN     all  --  anywhere             anywhere

Chain KUBE-MARK-DROP (0 references)
target     prot opt source               destination
MARK       all  --  anywhere             anywhere             MARK or 0x8000

Chain KUBE-MARK-MASQ (7 references)
target     prot opt source               destination
MARK       all  --  anywhere             anywhere             MARK or 0x4000

Chain KUBE-NODEPORTS (1 references)
target     prot opt source               destination
KUBE-MARK-MASQ  tcp  --  anywhere             anywhere             /* work/saythx-redis: */ tcp dpt:31269
KUBE-SVC-SMQNAAUIAENDDGYQ  tcp  --  anywhere             anywhere             /* work/saythx-redis: */ tcp dpt:31269

Chain KUBE-POSTROUTING (1 references)
target     prot opt source               destination
MASQUERADE  all  --  anywhere             anywhere             /* kubernetes service traffic requiring SNAT */ mark match 0x4000/0x4000

Chain KUBE-SEP-2LZPYBS4HUAJKDFL (1 references)
target     prot opt source               destination
KUBE-MARK-MASQ  all  --  10.32.0.2            anywhere             /* kube-system/kube-dns:dns-tcp */
DNAT       tcp  --  anywhere             anywhere             /* kube-system/kube-dns:dns-tcp */ tcp to:10.32.0.2:53

Chain KUBE-SEP-3E4LNQKKWZF7G6SH (1 references)
target     prot opt source               destination
KUBE-MARK-MASQ  all  --  10.32.0.1            anywhere             /* kube-system/kube-dns:dns-tcp */
DNAT       tcp  --  anywhere             anywhere             /* kube-system/kube-dns:dns-tcp */ tcp to:10.32.0.1:53

Chain KUBE-SEP-3IDG7DUGN3QC2UZF (1 references)
target     prot opt source               destination
KUBE-MARK-MASQ  all  --  172.17.0.120         anywhere             /* default/kubernetes:https */
DNAT       tcp  --  anywhere             anywhere             /* default/kubernetes:https */ tcp to:172.17.0.120:6443

Chain KUBE-SEP-JZWS2VPNIEMNMNB2 (1 references)
target     prot opt source               destination
KUBE-MARK-MASQ  all  --  10.32.0.2            anywhere             /* kube-system/kube-dns:dns */
DNAT       udp  --  anywhere             anywhere             /* kube-system/kube-dns:dns */ udp to:10.32.0.2:53

Chain KUBE-SEP-OEY6JJQSBCQPRKHS (1 references)
target     prot opt source               destination
KUBE-MARK-MASQ  all  --  10.32.0.1            anywhere             /* kube-system/kube-dns:dns */
DNAT       udp  --  anywhere             anywhere             /* kube-system/kube-dns:dns */ udp to:10.32.0.1:53

Chain KUBE-SEP-QX7VDAS5KDY6V3EV (1 references)
target     prot opt source               destination
KUBE-MARK-MASQ  all  --  10.32.0.2            anywhere             /* work/saythx-redis: */
DNAT       tcp  --  anywhere             anywhere             /* work/saythx-redis: */ tcp to:10.32.0.2:6379

Chain KUBE-SERVICES (2 references)
target     prot opt source               destination
KUBE-SVC-SMQNAAUIAENDDGYQ  tcp  --  anywhere             10.103.193.175       /* work/saythx-redis: cluster IP */ tcp dpt:6379
KUBE-NODEPORTS  all  --  anywhere             anywhere             /* kubernetes service nodeports; NOTE: this must be the last rule in this chain */ ADDRTYPE match dst-type LOCAL

Chain KUBE-SVC-ERIFXISQEP7F7OF4 (1 references)
target     prot opt source               destination
KUBE-SEP-3E4LNQKKWZF7G6SH  all  --  anywhere             anywhere             /* kube-system/kube-dns:dns-tcp */ statistic mode random probability 0.50000000000
KUBE-SEP-2LZPYBS4HUAJKDFL  all  --  anywhere             anywhere             /* kube-system/kube-dns:dns-tcp */

Chain KUBE-SVC-SMQNAAUIAENDDGYQ (2 references)
target     prot opt source               destination
KUBE-SEP-QX7VDAS5KDY6V3EV  all  --  anywhere             anywhere             /* work/saythx-redis: */
</code></pre>
<p>以上输出已经尽量删掉了无关的内容。</p>
<p>当开始访问的时候先要经过 <code>PREROUTING</code> 链，转到 <code>KUBE-SERVICES</code> 链，当查询到匹配的规则之后，请求将转向 <code>KUBE-SVC-SMQNAAUIAENDDGYQ</code> 链，进而到达 <code>KUBE-SEP-QX7VDAS5KDY6V3EV</code> 对应于我们的 <code>Pod</code>。(注：为了简洁，上述 iptables 规则是部署一个 <code>Pod</code> 时的场景)</p>
<p>当搞懂了这些之后，如果你想了解这些 <code>iptables</code> 规则实际又是如何创建和维护的，那可以参考下 <code>proxier</code> 的具体实现，这里不再展开。</p>
<h2>总结</h2>
<p>本节中我们介绍了 <code>kube-proxy</code> 的主要功能和基本流程，了解到了它对于服务注册发现和代理访问等起到了很大的作用。而它在 Linux 下的代理模式也有 <code>userspace</code>，<code>iptables</code> 和 <code>ipvs</code> 等。</p>
<p>默认情况下我们使用 <code>iptables</code> 的代理模式，当创建新的 <code>Service</code> ，或者 <code>Pod</code> 进行变化时，<code>kube-proxy</code> 便会去维护 <code>iptables</code> 规则，以确保请求可以正确的到达后端服务。</p>
<p>当然，本节中并没有提到 <code>kube-proxy</code> 的 <code>session affinity</code> 相关的特性，如有需要可进行下尝试。</p>
<p>下节，我们将介绍实际运行着容器的 <code>Docker</code>，大致了解下在 K8S 中它所起的作用，及他们之间的交互方式。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="16&#32;庖丁解牛：kubelet.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="18&#32;&#32;庖丁解牛：Container&#32;Runtime&#32;（Docker）.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346169c4e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
