<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>06 集群管理：初识 kubectl.md</title>
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

                    <a class="current-tab" href="06&#32;集群管理：初识&#32;kubectl.md">06 集群管理：初识 kubectl.md</a>
                    

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
                        <div><h1>06 集群管理：初识 kubectl</h1>
<p>从本节开始，我们来学习 K8S 集群管理相关的知识。通过前面的学习，我们知道 K8S 遵循 C/S 架构，官方也提供了 CLI 工具 <code>kubectl</code> 用于完成大多数集群管理相关的功能。当然凡是你可以通过 <code>kubectl</code> 完成的与集群交互的功能，都可以直接通过 API 完成。</p>
<p>对于我们来说 <code>kubectl</code> 并不陌生，在第 3 章讲 K8S 整体架构时，我们首次提到了它。在第 4 章和第 5 章介绍了两种安装 <code>kubectl</code> 的方式故而本章不再赘述安装的部分。</p>
<h2>整体概览</h2>
<p>首先我们在终端下执行下 <code>kubectl</code>:</p>
<pre><code>➜  ~ kubectl                
kubectl controls the Kubernetes cluster manager.
...
Usage:
  kubectl [flags] [options]
</code></pre>
<p><code>kubectl</code> 已经将命令做了基本的归类，同时显示了其一般的用法 <code>kubectl [flags] [options]</code> 。</p>
<p>使用 <code>kubectl options</code> 可以看到所有全局可用的配置项。</p>
<h2>基础配置</h2>
<p>在我们的用户家目录，可以看到一个名为 <code>.kube/config</code> 的配置文件，我们来看下其中的内容（此处以本地的 minikube 集群为例）。</p>
<pre><code>➜  ~ ls $HOME/.kube/config 
/home/tao/.kube/config
➜  ~ cat $HOME/.kube/config
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/tao/.minikube/ca.crt
    server: https://192.168.99.101:8443
  name: minikube
contexts:
- context:
    cluster: minikube
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: /home/tao/.minikube/client.crt
    client-key: /home/tao/.minikube/client.key
</code></pre>
<p><code>$HOME/.kube/config</code> 中主要包含着：</p>
<ul>
<li>K8S 集群的 API 地址</li>
<li>用于认证的证书地址</li>
</ul>
<p>当然，我们在第 5 章时，也已经说过，也可以使用 <code>--kubeconfig</code> 或者环境变量 <code>KUBECONFIG</code> 来传递配置文件。</p>
<p>另外如果你并不想使用配置文件的话，你也可以通过使用直接传递相关参数来使用，例如：</p>
<pre><code>➜  ~ kubectl --client-key='/home/tao/.minikube/client.key' --client-certificate='/home/tao/.minikube/client.crt' --server='https://192.168.99.101:8443'  get nodes
NAME       STATUS    ROLES     AGE       VERSION
minikube   Ready     master    2d        v1.11.3
</code></pre>
<h2>从 <code>get</code> 说起</h2>
<p>无论是第 4 章还是第 5 章，当我们创建集群后，我们都做了两个相同的事情，一个是执行 <code>kubectl get nodes</code> 另一个则是 <code>kubectl cluster-info</code>，我们先从查看集群内 <code>Node</code> 开始。</p>
<p>这里我们使用了一个本地已创建好的 <code>minikube</code> 集群。</p>
<pre><code>➜  ~ kubectl get nodes
NAME       STATUS    ROLES     AGE       VERSION
minikube   Ready     master    2d        v1.11.3
➜  ~ kubectl get node
NAME       STATUS    ROLES     AGE       VERSION
minikube   Ready     master    2d        v1.11.3
➜  ~ kubectl get no
NAME       STATUS    ROLES     AGE       VERSION
minikube   Ready     master    2d        v1.11.3
</code></pre>
<p>可以看到以上三种“名称”均可获取当前集群内 <code>Node</code> 信息。这是为了便于使用而增加的别名和缩写。</p>
<p>如果我们想要看到更详细的信息呢？可以通过传递 <code>-o</code> 参数以得到不同格式的输出。</p>
<pre><code>➜  ~ kubectl get nodes -o wide 
NAME       STATUS    ROLES     AGE       VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE            KERNEL-VERSION   CONTAINER-RUNTIME
minikube   Ready     master    2d        v1.11.3   10.0.2.15     &lt;none&gt;        Buildroot 2018.05   4.15.0           docker://17.12.1-ce
</code></pre>
<p>当然也可以传递 <code>-o yaml</code> 或者 <code>-o json</code> 得到更加详尽的信息。</p>
<p>使用 <code>-o json</code> 将内容以 JSON 格式输出时，可以配合 <a href="https://stedolan.github.io/jq/"><code>jq</code></a> 进行内容提取。例如：</p>
<pre><code>➜  ~ kubectl get nodes -o json | jq &quot;.items[] | {name: .metadata.name} + .status.nodeInfo&quot;
{
  &quot;name&quot;: &quot;minikube&quot;,
  &quot;architecture&quot;: &quot;amd64&quot;,
  &quot;bootID&quot;: &quot;d675d75b-e58e-40db-8910-6e5dda9e7cf9&quot;,
  &quot;containerRuntimeVersion&quot;: &quot;docker://17.12.1-ce&quot;,
  &quot;kernelVersion&quot;: &quot;4.15.0&quot;,
  &quot;kubeProxyVersion&quot;: &quot;v1.11.3&quot;,
  &quot;kubeletVersion&quot;: &quot;v1.11.3&quot;,
  &quot;machineID&quot;: &quot;078e2d22629747178397e29cf1c96cc7&quot;,
  &quot;operatingSystem&quot;: &quot;linux&quot;,
  &quot;osImage&quot;: &quot;Buildroot 2018.05&quot;,
  &quot;systemUUID&quot;: &quot;4073906D-69A1-46EE-A08C-0252D9F79893&quot;
}
</code></pre>
<p>以此方法可得到 <code>Node</code> 的基础信息。</p>
<p>那么除了 <code>Node</code> 外我们还可以查看那些资源或别名呢？可以通过 <code>kubectl api-resources</code> 查看服务端支持的 API 资源及别名和描述等信息。</p>
<h2>答疑解惑 <code>explain</code></h2>
<p>当通过上面的命令拿到所有支持的 API 资源列表后，虽然后面基本都有一个简单的说明，是不是仍然感觉一头雾水？</p>
<p>别担心，在我们使用 Linux 的时候，我们有 <code>man</code> ，在使用 <code>kubectl</code> 的时候，我们除了 <code>--help</code> 外还有 <code>explain</code> 可帮我们进行说明。 例如：</p>
<pre><code>➜  ~ kubectl explain node                                                                                                              
KIND:     Node
VERSION:  v1

DESCRIPTION:              
     Node is a worker node in Kubernetes. Each node will have a unique
     identifier in the cache (i.e. in etcd).

# ... 省略输出
</code></pre>
<h2>总结</h2>
<p>本节我们大致介绍了 <code>kubectl</code> 的基础使用，尤其是最常见的 <code>get</code> 命令。可通过传递不同参数获取不同格式的输出，配合 <code>jq</code> 工具可方便的进行内容提取。</p>
<p>以及关于 <code>kubectl</code> 的配置文件和无配置文件下通过传递参数直接使用等。</p>
<p>对应于我们前面提到的 K8S 架构，本节相当于 <code>CURD</code> 中的 <code>R</code> 即查询。查询对于我们来说，既是我们了解集群的第一步，同时也是后续验证操作结果或集群状态必不可少的技能。</p>
<p>当然，你在集群管理中可能会遇到各种各样的问题，单纯依靠 <code>get</code> 并不足以定位问题，我们在第 21 节中将介绍 Troubleshoot 的思路及方法。</p>
<p>下节我们来学习关于 <code>C</code> 的部分，即创建。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="05&#32;动手实践：搭建一个&#32;Kubernetes&#32;集群&#32;-&#32;生产可用.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="07&#32;集群管理：以&#32;Redis&#32;为例-部署及访问.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345defe1570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
