<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13 庖丁解牛：etcd.md</title>
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

                    <a class="current-tab" href="13&#32;庖丁解牛：etcd.md">13 庖丁解牛：etcd.md</a>
                    

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
                        <div><h1>13 庖丁解牛：etcd</h1>
<h2>整体概览</h2>
<pre><code>+----------------------------------------------------------+          
| Master                                                   |          
|              +-------------------------+                 |          
|     +-------&gt;|        API Server       |&lt;--------+       |          
|     |        |                         |         |       |          
|     v        +-------------------------+         v       |          
|   +----------------+     ^      +--------------------+   |          
|   |                |     |      |                    |   |          
|   |   Scheduler    |     |      | Controller Manager |   |          
|   |                |     |      |                    |   |          
|   +----------------+     v      +--------------------+   |          
| +------------------------------------------------------+ |          
| |                                                      | |          
| |                Cluster state store                   | |          
| |                                                      | |          
| +------------------------------------------------------+ |          
+----------------------------------------------------------+          
</code></pre>
<p>在第 3 节《宏观认识：整体架构》 中，我们也认识到了 <code>etcd</code> 的存在，知道了 Master 是 K8S 是集群的大脑，而 <code>etcd</code> 则是大脑的核心。为什么这么说？本节我们一同来看看 <code>etcd</code> 为何如此重要。</p>
<h2><code>etcd</code> 是什么</h2>
<p>先摘录<a href="https://etcd.readthedocs.io/en/latest/faq.html#what-is-etcd">官方文档</a>的一句说明:</p>
<blockquote>
<p>etcd is a consistent distributed key-value store. Mainly used as a separate coordination service, in distributed systems. And designed to hold small amounts of data that can fit entirely in memory.</p>
</blockquote>
<p><code>etcd</code> 是由 CoreOS 团队发起的一个分布式，强一致的键值存储。它用 Go 语言编写，使用 <code>Raft</code> 协议作为一致性算法。多数情况下会用于分布式系统中的服务注册发现，或是用于存储系统的关键数据。</p>
<h2><code>etcd</code> 有什么作用</h2>
<p><code>etcd</code> 在 K8S 中，最主要的作用便是其高可用，强一致的键值存储以及监听机制。</p>
<p>在 <code>kube-apiserver</code> 收到对应请求经过一系列的处理后，最终如果是集群所需要存储的数据，便会存储至 <code>etcd</code> 中。主部分主要是集群状态信息和元信息。</p>
<p>我们来实际操作 K8S 集群中的 <code>etcd</code> 看下真实情况。</p>
<ul>
<li>查找集群中的 <code>etcd</code> Pod</li>
</ul>
<pre><code># 默认集群中的 etcd 会放到 kube-system Namespace 中
master $ kubectl -n kube-system get pods | grep etcd
etcd-master                      1/1       Running   0          1h
</code></pre>
<ul>
<li>进入该 Pod 并查看 <code>etcd</code> 集群的 <code>member</code></li>
</ul>
<pre><code>master $ kubectl -n kube-system exec -it etcd-master sh
/ # ETCDCTL_API=3 etcdctl --key=/etc/kubernetes/pki/etcd/server.key  --cert=/etc/kubernetes/pki/etcd/server.crt  --cacert=/etc/kubernetes/pki/etcd/ca.crt member list
a874c87fd42044f, started, master, https://127.0.0.1:2380, https://127.0.0.1:2379
</code></pre>
<p>这里由于在 K8S 1.11.3 中默认使用的是 <code>etcd</code> 3.2 版本，所以需要加入 <code>ETCDCTL_API=3</code> 的环境变量，且 <code>etcd</code> 从 2 到 3 很明显的一个变化也是使用上的变化，在 2 中是 HTTP 接口的。</p>
<p>我们通过传递证书等相关参数进去，完成校验，查看 <code>member</code> 。</p>
<ul>
<li>查看存储的元信息</li>
</ul>
<p><code>etcd</code> 中存储的 K8S 集群元信息基本都是 <code>/registry</code> 下，我们可通过下面的方式进行查看</p>
<pre><code>/ # ETCDCTL_API=3 etcdctl --key=/etc/kubernetes/pki/etcd/server.key  --cert=/etc/kubernetes/pki/etcd/server.crt  --cacert=/etc/kubernetes/pki/etcd/ca.crt get /registry --prefix --keys-only
/registry/apiregistration.k8s.io/apiservices/v1.
/registry/clusterroles/system:aggregate-to-admin
/registry/configmaps/kube-public/cluster-info
/registry/masterleases/172.17.0.53
/registry/namespaces/default
/registry/namespaces/kube-public
/registry/namespaces/kube-system
/registry/pods/kube-system/etcd-master
/registry/pods/kube-system/kube-apiserver-master
/registry/ranges/serviceips
/registry/ranges/servicenodeports
...
# 篇幅原因，删掉了很多输出
</code></pre>
<p>可以看到有各种类型的资源。我们直接以 Namespaces 为例。</p>
<ul>
<li>查看 Namespaces 信息</li>
</ul>
<pre><code>/ # ETCDCTL_API=3 etcdctl --key=/etc/kubernetes/pki/etcd/server.key  --cert=/etc/kubernetes/pki/etcd/server.crt  --cacert=/etc/kubernetes/pki/etcd/ca.crt get /registry/namespaces --prefix --keys-only
/registry/namespaces/default

/registry/namespaces/kube-public

/registry/namespaces/kube-system
</code></pre>
<ul>
<li>使用 <code>kubectl</code> 创建名为 <code>moelove</code> 的 Namespaces</li>
</ul>
<pre><code>master $ kubectl create  ns moelove
namespace/moelove created
</code></pre>
<ul>
<li>查看 Namespaces 信息</li>
</ul>
<pre><code>/ # ETCDCTL_API=3 etcdctl --key=/etc/kubernetes/pki/etcd/server.key  --cert=/etc/kubernetes/pki/etcd/server.crt  --cacert=/etc/kubernetes/pki/etcd/ca.crt get /registry/namespaces --prefix --keys-only
/registry/namespaces/default

/registry/namespaces/kube-public

/registry/namespaces/kube-system

/registry/namespaces/moelove
</code></pre>
<p>发现刚创建的 <code>moelove</code> 的 Namespaces 已经在 <code>etcd</code> 中了。</p>
<h2><code>etcd</code> 是如何被使用的</h2>
<p>首先，在 <code>staging/src/k8s.io/apiserver/pkg/server/options/etcd.go</code> 中，存在一处声明：</p>
<pre><code>var storageTypes = sets.NewString(
	storagebackend.StorageTypeUnset,
	storagebackend.StorageTypeETCD2,
	storagebackend.StorageTypeETCD3,
)
</code></pre>
<p><strong>在 1.13 发布时，etcd 2 的相关代码已经移除，其中就包含上面声明中的 storagebackend.StorageTypeETCD2</strong></p>
<p>这里是在过渡期间为了同时兼容 <code>etcd</code> 2 和 3 而增加的。</p>
<p>我们来看下实际对各类资源的操作，还是以对 <code>Namespace</code> 的操作为例：代码在 <code>pkg/registry/core/namespace/storage/storage.go</code> 中，</p>
<p>比如，<code>Get</code>：</p>
<pre><code>func (r *REST) Get(ctx context.Context, name string, options *metav1.GetOptions) (runtime.Object, error) {
	return r.store.Get(ctx, name, options)
}
</code></pre>
<p>而 <code>REST</code> 则是这样定义的：</p>
<pre><code>type REST struct {
	store  *genericregistry.Store
	status *genericregistry.Store
}
</code></pre>
<p>通过 <code>REST</code> 实现了一个 <code>RESTStorage</code>，实际使用时，也是调用了 <code>staging/src/k8s.io/apiserver/pkg/registry/generic/registry/store.go</code> 对接口的封装。</p>
<pre><code>func (e *Store) Get(ctx context.Context, name string, options *metav1.GetOptions) (runtime.Object, error) {
	obj := e.NewFunc()
	key, err := e.KeyFunc(ctx, name)
	if err != nil {
		return nil, err
	}
	if err := e.Storage.Get(ctx, key, options.ResourceVersion, obj, false); err != nil {
		return nil, storeerr.InterpretGetError(err, e.qualifiedResourceFromContext(ctx), name)
	}
	if e.Decorator != nil {
		if err := e.Decorator(obj); err != nil {
			return nil, err
		}
	}
	return obj, nil
}
</code></pre>
<p>在该处实现了对各类基本方法的封装，各种资源类型都会统一去调用。而更上层则是对 <code>storagebackend</code> 的统一封装，最终会调用 <code>etcd</code> 客户端的实现完成想对应的操作，这里就不再多展开了。</p>
<h2>总结</h2>
<p>在本节中，我们介绍了 <code>etcd</code> 以及它在 K8S 中的作用以及如何使用。我们还介绍了如何通过 <code>etcdctl</code> 工具去操作 <code>etcd</code>。</p>
<p>在某些极端情况下，也许你需要通过直接操作 <code>etcd</code> 集群去变更数据，这里没有介绍所有的操作命令，感兴趣的可以自行通过下方的链接看官方文档进行学习。</p>
<p>但通常情况下，不建议直接操作 <code>etcd</code> ，除非你已经明确自己在做什么。</p>
<p>另外，由于 <code>etcd</code> 集群使用 <code>Raft</code> 一致性算法，通常情况下 <code>etcd</code> 集群需要部署奇数个节点，如 3，5，7 等。<code>etcd</code> 集群维护也相对容易，很容易可以做成高可用集群。（这也是保障 K8S 集群高可用的重要一环）</p>
<p>学习了 <code>etcd</code> 之后，下节我们来学习同样很重要的一个组件 <code>Controller Manager</code>，学习它是如何保障集群符合预期状态的。</p>
<h2>参考链接</h2>
<ul>
<li><a href="https://etcd.readthedocs.io/en/latest/faq.html#what-is-etcd">What is etcd</a></li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;庖丁解牛：kube-apiserver.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;庖丁解牛：controller-manager.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346056b9970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
