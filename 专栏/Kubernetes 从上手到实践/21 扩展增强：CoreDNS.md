<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>21 扩展增强：CoreDNS.md</title>
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

                    
                    <a href="18&#32;&#32;庖丁解牛：Container&#32;Runtime&#32;（Docker）.md">18  庖丁解牛：Container Runtime （Docker）.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;Troubleshoot.md">19 Troubleshoot.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;扩展增强：Dashboard.md">20 扩展增强：Dashboard.md</a>

                </li>
                <li>

                    <a class="current-tab" href="21&#32;扩展增强：CoreDNS.md">21 扩展增强：CoreDNS.md</a>
                    

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
                        <div><h1>21 扩展增强：CoreDNS</h1>
<h2>整体概览</h2>
<p>通过前面的学习，我们知道在 K8S 中有一套默认的<a href="https://github.com/kubernetes/dns">集群内 DNS 服务</a>，我们通常把它叫做 <code>kube-dns</code>，它基于 SkyDNS，为我们在服务注册发现方面提供了很大的便利。</p>
<p>比如，在我们的示例项目 <a href="https://github.com/tao12345666333/saythx">SayThx</a> 中，各组件便是依赖 DNS 进行彼此间的调用。</p>
<p>本节，我们将介绍的 <a href="https://coredns.io/">CoreDNS</a> 是 CNCF 旗下又一孵化项目，在 K8S 1.9 版本中加入并进入 Alpha 阶段。我们当前是以 K8S 1.11 的版本进行介绍，它并不是默认的 DNS 服务，但是<a href="https://github.com/kubernetes/enhancements/issues/427">它作为 K8S 的 DNS 插件的功能已经 GA</a> 。</p>
<p>CoreDNS 在 K8S 1.13 版本中才正式成为<a href="https://kubernetes.io/blog/2018/12/03/kubernetes-1-13-release-announcement/">默认的 DNS 服务</a>。</p>
<h2>CoreDNS 是什么</h2>
<p>首先，我们需要明确 CoreDNS 是一个独立项目，它不仅可支持在 K8S 中使用，你也可以在你任何需要 DNS 服务的时候使用它。</p>
<p>CoreDNS 使用 Go 语言实现，部署非常方便。</p>
<p>它的扩展性很强，很多功能特性都是通过插件完成的，它不仅有大量的<a href="https://coredns.io/plugins/">内置插件</a>，同时也有很丰富的<a href="https://coredns.io/explugins/">第三方插件</a>。甚至你自己<a href="https://coredns.io/2016/12/19/writing-plugins-for-coredns/">写一个插件</a>也非常的容易。</p>
<h2>如何安装使用 CoreDNS</h2>
<p>我们这里主要是为了说明如何在 K8S 环境中使用它，所以对于独立安装部署它不做说明。</p>
<p>本小册中我们使用的是 K8S 1.11 版本，在第 5 小节 《搭建 Kubernetes 集群》中，我们介绍了使用 <code>kubeadm</code> 搭建集群。</p>
<p>使用 <code>kubeadm</code> 创建集群时候 <code>kubeadm init</code> 可以传递 <code>--feature-gates</code> 参数，用于启用一些额外的特性。</p>
<p>比如在之前版本中，我们可以通过 <code>kubeadm init --feature-gates CoreDNS=true</code> 在创建集群时候启用 CoreDNS。</p>
<p>而在 1.11 版本中，使用 <code>kubeadm</code> 创建集群时 <code>CoreDNS</code> 已经被默认启用，这也从侧面证明了 CoreDNS 在 K8S 中达到了生产可用的状态。</p>
<p>我们来看一下创建集群时的日志输出：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="d4a6bbbba094b9b5a7a0b1a6">[email&#160;protected]</a> ~]# kubeadm init
[init] using Kubernetes version: v1.11.3               
[preflight] running pre-flight checks
...
[bootstraptoken] creating the &quot;cluster-info&quot; ConfigMap in the &quot;kube-public&quot; namespace
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

Your Kubernetes master has initialized successfully!
</code></pre>
<p>可以看到创建时已经启用了 CoreDNS 的扩展，待集群创建完成后，可用过以下方式进行查看：</p>
<pre><code>master $ kubectl -n kube-system get all  -l k8s-app=kube-dns -o wide
NAME                           READY     STATUS    RESTARTS   AGE       IP          NODE      NOMINATED NODE
pod/coredns-78fcdf6894-5zbx4   1/1       Running   0          1h        10.32.0.3   node01    &lt;none&gt;
pod/coredns-78fcdf6894-cxdw8   1/1       Running   0          1h        10.32.0.2   node01    &lt;none&gt;

NAME               TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)         AGE       SELECTOR
service/kube-dns   ClusterIP   10.96.0.10   &lt;none&gt;        53/UDP,53/TCP   1h        k8s-app=kube-dns

NAME                      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE       CONTAINERS   IMAGES                     SELECTOR
deployment.apps/coredns   2         2         2            2           1h        coredns      k8s.gcr.io/coredns:1.1.3   k8s-app=kube-dns

NAME                                 DESIRED   CURRENT   READY     AGE       CONTAINERS   IMAGES                   SELECTOR
replicaset.apps/coredns-78fcdf6894   2         2         2         1h        coredns      k8s.gcr.io/coredns:1.1.3   k8s-app=kube-dns,pod-template-hash=3497892450
</code></pre>
<p>这里主要是为了兼容 K8S 原有的 <code>kube-dns</code> 所以标签和 <code>Service</code> 的名字都还使用了 <code>kube-dns</code>，但实际在运行的则是 CoreDNS。</p>
<h2>验证 CoreDNS 功能</h2>
<p>从上面的输出我们看到 CoreDNS 的 <code>Pod</code> 运行正常，现在测试下它是否能正确解析。仍然以我们的示例项目 <a href="https://github.com/tao12345666333/saythx">SayThx</a> 为例，先 clone 项目，进入到项目的 deploy 目录中。</p>
<pre><code>master $ cd saythx/deploy/
master $ ls
backend-deployment.yaml  frontend-deployment.yaml  namespace.yaml         redis-service.yaml
backend-service.yaml     frontend-service.yaml     redis-deployment.yaml  work-deployment.yaml
master $ kubectl apply -f namespace.yaml
namespace/work created
master $ kubectl apply -f redis-deployment.yaml
deployment.apps/saythx-redis created
master $ kubectl apply -f redis-service.yaml
service/saythx-redis created
</code></pre>
<ul>
<li>查看其部署情况：</li>
</ul>
<pre><code>master $ kubectl -n work get all
NAME                               READY     STATUS    RESTARTS   AGE
pod/saythx-redis-8558c7d7d-8v4lp   1/1       Running   0          2m

NAME                   TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/saythx-redis   NodePort   10.109.215.147   &lt;none&gt;        6379:31438/TCP   2m

NAME                           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/saythx-redis   1         1         1            1           2m

NAME                                     DESIRED   CURRENT   READY     AGE
replicaset.apps/saythx-redis-8558c7d7d   1         1         1         2m
</code></pre>
<ul>
<li>验证 DNS 是否正确解析:</li>
</ul>
<pre><code># 使用 AlpineLinux 的镜像创建一个 Pod 并进入其中
master $ kubectl run alpine -it --rm --restart='Never' --image='alpine' sh
If you don't see a command prompt, try pressing enter.
/ # apk add --no-cache bind-tools
fetch http://dl-cdn.alpinelinux.org/alpine/v3.8/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.8/community/x86_64/APKINDEX.tar.gz
(1/5) Installing libgcc (6.4.0-r9)
(2/5) Installing json-c (0.13.1-r0)
(3/5) Installing libxml2 (2.9.8-r1)
(4/5) Installing bind-libs (9.12.3-r0)
(5/5) Installing bind-tools (9.12.3-r0)
Executing busybox-1.28.4-r2.trigger
OK: 9 MiB in 18 packages

# 安装完 dig 命令所在包之后，使用 dig 命令进行验证
/ # dig @10.32.0.2 saythx-redis.work.svc.cluster.local +noall +answer

; &lt;&lt;&gt;&gt; DiG 9.12.3 &lt;&lt;&gt;&gt; @10.32.0.2 saythx-redis.work.svc.cluster.local +noall +answer
; (1 server found)
;; global options: +cmd
saythx-redis.work.svc.cluster.local. 5 IN A     10.109.215.147
</code></pre>
<p>通过以上操作，可以看到相应的 <code>Service</code> 记录可被正确解析。这里有几个点需要注意：</p>
<ul>
<li>
<p>域名解析是可跨 <code>Namespace</code> 的</p>
<p>刚才的示例中，我们没有指定 <code>Namespace</code> 所以刚才我们所在的 <code>Namespace</code> 是 <code>default</code>。而我们的解析实验成功了。说明 CoreDNS 的解析是全局的。<strong>虽然解析是全局的，但不代表网络互通</strong></p>
</li>
<li>
<p>域名有特定格式</p>
<p>可以看到刚才我们使用的完整域名是 <code>saythx-redis.work.svc.cluster.local</code> , 注意开头的便是 <strong>Service 名.Namespace 名</strong> 当然，我们也可以直接通过 <code>host</code> 命令查询:</p>
<pre><code>/ # host -t srv  saythx-redis.work
saythx-redis.work.svc.cluster.local has SRV record 0 100 6379 saythx-redis.work.svc.cluster.local.
</code></pre>
</li>
</ul>
<h2>配置和监控</h2>
<p>CoreDNS 使用 <code>ConfigMap</code> 的方式进行配置，但是如果更改了配置，<code>Pod</code> 重启后才会生效。</p>
<p>我们通过以下命令可查看其配置：</p>
<pre><code>master $ kubectl -n kube-system get configmap coredns -o yaml
apiVersion: v1
data:
  Corefile: |
    .:53 {
        errors
        health
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           upstream
           fallthrough in-addr.arpa ip6.arpa
        }
        prometheus :9153
        proxy . /etc/resolv.conf
        cache 30
        reload
    }
kind: ConfigMap
metadata:
  creationTimestamp: 2018-12-22T16:45:47Z
  name: coredns
  namespace: kube-system
  resourceVersion: &quot;217&quot;
  selfLink: /api/v1/namespaces/kube-system/configmaps/coredns
  uid: 0882e51b-0609-11e9-b25e-0242ac110057
</code></pre>
<p><code>Corefile</code> 便是它的配置文件，可以看到它启动了类似 <code>kubernetes</code>, <code>prometheus</code> 等插件。</p>
<p>注意 <code>kubernetes</code> 插件的配置，使用的域是 <code>cluster.local</code> ，这也是上面我们提到域名格式时候后半部分未解释的部分。</p>
<p>至于 <code>prometheus</code> 插件，则是监听在 9153 端口上提供了符合 Prometheus 标准的 metrics 接口，可用于监控等。关于监控的部分，可参考第 23 节。</p>
<h2>总结</h2>
<p>在本节中，我们介绍了 CoreDNS 的基本情况，它是以 Go 编写的灵活可扩展的 DNS 服务器。</p>
<p>使用 CoreDNS 代替 kube-dns 主要是为了解决一些 kube-dns 时期的问题，比如说原先 kube-dns 的时候，一个 Pod 中还需要包含 <code>kube-dns</code>, <code>sidecar</code> 和 <code>dnsmasq</code> 的容器，而每当 <code>dnsmasq</code> 出现漏洞时，就不得不让 K8S 发个安全补丁才能进行更新。</p>
<p>CoreDNS 有丰富的插件，可以满足更多样的应用需求，同时 <code>kubernetes</code> 插件还包含了一些独特的功能，比如 Pod 验证之类的，可增加安全性。</p>
<p>同时 CoreDNS 在 1.13 版本中会作为默认的 DNS 服务器使用，所以应该给它更多的关注。</p>
<p>在下节，我们将介绍 <code>Ingress</code>，看看如果使用不同于之前使用的 <code>NodePort</code> 的方式将服务暴露于外部。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="20&#32;扩展增强：Dashboard.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="22&#32;服务增强：Ingress.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b43462a5a7e70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
