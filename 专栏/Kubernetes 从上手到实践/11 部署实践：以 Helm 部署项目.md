<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>11 部署实践：以 Helm 部署项目.md</title>
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

                    <a class="current-tab" href="11&#32;部署实践：以&#32;Helm&#32;部署项目.md">11 部署实践：以 Helm 部署项目.md</a>
                    

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
                        <div><h1>11 部署实践：以 Helm 部署项目</h1>
<h2>概览</h2>
<p>上节，我们学习到了 Helm 的基础概念和工作原理，本节我们将 Helm 用于我们的实际项目，编写 Helm <code>chart</code> 以及通过 Helm 进行部署。</p>
<h2>Helm chart</h2>
<p>上节我们解释过 <code>chart</code> 的含义，现在我们要将项目使用 Helm 部署，那么首先，我们需要创建一个 <code>chart</code>。</p>
<h3>Chart 结构</h3>
<p>在我们项目的根目录下，通过以下命令创建一个 <code>chart</code>。</p>
<pre><code>➜  saythx git:(master) helm create saythx
Creating saythx
➜  saythx git:(master) ✗ tree -a saythx
saythx
├── charts
├── Chart.yaml
├── .helmignore
├── templates
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   ├── ingress.yaml
│   ├── NOTES.txt
│   └── service.yaml
└── values.yaml

2 directories, 8 files
</code></pre>
<p>创建完成后，我们可以看到默认创建的 <code>chart</code> 中包含了几个文件和目录。我们先对其进行解释。</p>
<h4>Chart.yaml</h4>
<pre><code>➜  saythx git:(master) ✗ cat saythx/Chart.yaml
apiVersion: v1
appVersion: &quot;1.0&quot;
description: A Helm chart for Kubernetes
name: saythx
version: 0.1.0
</code></pre>
<p>这个文件是每个 <code>chart</code> 必不可少的一个文件，其中包含着几个重要的属性，如：</p>
<ul>
<li><code>apiVersion</code>：目前版本都为 <code>v1</code></li>
<li><code>appVersion</code>：这是应用的版本号，需要与 <code>apiVersion</code>， <code>version</code> 等字段注意区分</li>
<li><code>name</code>: 通常要求 <code>chart</code> 的名字必须和它所在目录保持一致，且此字段必须</li>
<li><code>version</code>：表明当前 <code>chart</code> 的版本号，会直接影响 <code>Release</code> 的记录，且此字段必须</li>
<li><code>description</code>：描述</li>
</ul>
<h4>charts</h4>
<p><code>charts</code> 文件夹是用于存放依赖的 <code>chart</code> 的。当有依赖需要管理时，可添加 <code>requirements.yaml</code> 文件，可用于管理项目内或者外部的依赖。</p>
<h4>.helmignore</h4>
<p><code>.helmignore</code> 类似于 <code>.gitignore</code> 和 <code>.dockerignore</code> 之类的，用于忽略掉一些不想包含在 <code>chart</code> 内的文件。</p>
<h4>templates</h4>
<p><code>templates</code> 文件夹内存放着 <code>chart</code> 所使用的模板文件，也是 <code>chart</code> 的实际执行内容。在使用 <code>chart</code> 进行安装的时候，会将 下面介绍的 <code>values.yaml</code> 中的配置项与 <code>templates</code> 中的模板进行组装，生成最终要执行的配置文件。</p>
<p><code>templates</code> 中，推荐命名应该清晰，如 <code>xx-deployment.yaml</code>，中间使用 <code>-</code> 进行分割，避免使用驼峰式命名。</p>
<p><code>Notes.txt</code> 文件在 <code>helm install</code> 完成后，会进行回显，可用于解释说明如何访问服务等。</p>
<h4>values.yaml</h4>
<p><code>values.yaml</code> 存放着项目的一些可配置项，如镜像的名称或者 tag 之类的。作用就是用于和模板进行组装。</p>
<h3>编写 chart</h3>
<p>了解完结构之后，我们来实际编写我们的 chart 。所有完整的代码可在 <a href="https://github.com/tao12345666333/saythx">SayThx 项目</a> 获取。</p>
<pre><code># Chart.yaml
apiVersion: v1
appVersion: &quot;1.0&quot;
description: A Helm chart for SayThx.
name: saythx
version: 0.1.0
maintainers:
  - name: Jintao Zhang
</code></pre>
<p>可添加 <code>maintainers</code> 字段，表示维护者。</p>
<pre><code># values.yaml

# backend is the values for backend
backend:
  image: taobeier/saythx-be
  tag: &quot;1.0&quot;
  pullPolicy: IfNotPresent
  replicas: 1

# namespace is the values for deploy namespace
namespace: work

# service.type is the values for service type
service:
  type: NodePort
</code></pre>
<p><code>values.yaml</code> 文件中定义了我们预期哪些东西是可配置的，比如 <code>namespace</code> 以及镜像名称 tag 等。这里只是贴出了部分内容，仅做说明使用，完整内容可查看我们的<a href="https://github.com/tao12345666333/saythx">示例项目</a> 。</p>
<p>写 <code>values.yaml</code> 文件的时候，由于是使用 <code>YAML</code> 格式的配置，所以它非常的灵活，即可以使用如上面例子中的 <code>backend</code> 那种字典类型的， 也可以写成简单的 k-v 形式。但通常来讲，应该尽可能的将它写的清晰明确。并且容易被替换。</p>
<pre><code># templates/backend-service.yaml 

apiVersion: v1
kind: Service
metadata:
  labels:
    app: backend
  name: saythx-backend
  namespace: {{ .Values.namespace }}
spec:
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 8080
  selector:
    app: backend
  type: {{ .Values.service.type }}
</code></pre>
<p>将我们之前写的部署文件模板化，与配置项进行组装。</p>
<pre><code>1. Get the application URL by running these commands:
{{- if contains &quot;NodePort&quot; .Values.service.type }}
  export NODE_PORT=$(kubectl get --namespace {{ .Values.namespace }} -o jsonpath=&quot;{.spec.ports[0].nodePort}&quot; services saythx-frontend)
  export NODE_IP=$(kubectl get nodes --namespace {{ .Values.namespace }} -o jsonpath=&quot;{.items[0].status.addresses[0].address}&quot;)
  echo http://$NODE_IP:$NODE_PORT
{{- else if contains &quot;ClusterIP&quot; .Values.service.type }}
  export POD_NAME=$(kubectl get pods --namespace {{ .Values.namespace }} -l &quot;app=frontend&quot; -o jsonpath=&quot;{.items[0].metadata.name}&quot;)
  echo &quot;Visit http://127.0.0.1:8080 to use your application&quot;
  kubectl --namespace {{ .Values.namespace }} port-forward $POD_NAME 8080:80
{{- end }}
</code></pre>
<p>上面这是 <code>NOTES.txt</code> 文件内的内容。 这些内容会在 <code>helm install</code> 执行成功后显示在终端，用于说明服务如何访问或者其他注意事项等。</p>
<p>当然，这里的内容主要是为了说明如何编写 <code>chart</code> ，在实践中，尽量避免硬编码配置在里面。</p>
<h2>部署</h2>
<h3>直接部署</h3>
<p>Helm 的 <code>chart</code> 可以直接在源码目录下通过 <code>helm install</code> 完成部署。例如：</p>
<pre><code>➜  saythx helm install saythx
NAME:   handy-seastar
LAST DEPLOYED: Tue Nov 20 23:33:42 2018
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==&gt; v1/Namespace
NAME  STATUS  AGE
work  Active  1s

==&gt; v1/Service
NAME             TYPE      CLUSTER-IP      EXTERNAL-IP  PORT(S)         AGE
saythx-backend   NodePort  10.102.206.213  &lt;none&gt;       8080:30663/TCP  0s
saythx-frontend  NodePort  10.96.109.45    &lt;none&gt;       80:30300/TCP    0s
saythx-redis     NodePort  10.97.174.8     &lt;none&gt;       6379:30589/TCP  0s

==&gt; v1/Deployment
NAME             DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
saythx-backend   1        1        1           0          0s
saythx-frontend  1        1        1           0          0s
saythx-redis     1        1        1           0          0s
saythx-work      1        1        1           0          0s

==&gt; v1/Pod(related)
NAME                              READY  STATUS             RESTARTS  AGE
saythx-backend-7f6d86d9c8-xqttg   0/1    ContainerCreating  0         0s
saythx-frontend-777fc64997-9zmq6  0/1    Pending            0         0s
saythx-redis-8558c7d7d-lh5df      0/1    ContainerCreating  0         0s
saythx-work-9b4446d84-c2pr4       0/1    ContainerCreating  0         0s

NOTES:
1. Get the application URL by running these commands:
  export NODE_PORT=$(kubectl get --namespace work -o jsonpath=&quot;{.spec.ports[0].nodePort}&quot; services saythx-frontend)
  export NODE_IP=$(kubectl get nodes --namespace work -o jsonpath=&quot;{.items[0].status.addresses[0].address}&quot;)
  echo http://$NODE_IP:$NODE_PORT
</code></pre>
<h3>打包</h3>
<p>当然，我们也可以将 <code>chart</code> 打包，以便于分发。</p>
<pre><code>➜  saythx helm package saythx 
Successfully packaged chart and saved it to: /root/saythx/saythx-0.1.0.tgz
</code></pre>
<p>可以看到打包时是按照 <code>chart</code> 的名字加版本号进行命名的。</p>
<p>至于部署，和前面没什么太大区别， <code>helm install saythx-0.1.0.tgz</code> 即可。</p>
<h3>访问服务</h3>
<p>前面在部署完成后，有一些返回信息，我们来按照其内容访问我们的服务：</p>
<pre><code>➜  saythx export NODE_PORT=$(kubectl get --namespace work -o jsonpath=&quot;{.spec.ports[0].nodePort}&quot; services saythx-frontend)
➜  saythx export NODE_IP=$(kubectl get nodes --namespace work -o jsonpath=&quot;{.items[0].status.addresses[0].address}&quot;)
➜  saythx echo http://$NODE_IP:$NODE_PORT
http://172.17.0.5:30300
➜  saythx curl http://172.17.0.5:30300
&lt;!DOCTYPE html&gt;&lt;html lang=en&gt;&lt;head&gt;&lt;meta charset=utf-8&gt;&lt;meta http-equiv=X-UA-Compatible content=&quot;IE=edge&quot;&gt;&lt;meta name=viewport content=&quot;width=device-width,initial-scale=1&quot;&gt;&lt;link rel=icon href=/favicon.ico&gt;&lt;title&gt;fe&lt;/title&gt;&lt;link href=/css/app.0a6f0b04.css rel=preload as=style&gt;&lt;link href=/css/chunk-vendors.ea3fa8e3.css rel=preload as=style&gt;&lt;link href=/js/app.ee469174.js rel=preload as=script&gt;&lt;link href=/js/chunk-vendors.14b9b088.js rel=preload as=script&gt;&lt;link href=/css/chunk-vendors.ea3fa8e3.css rel=stylesheet&gt;&lt;link href=/css/app.0a6f0b04.css rel=stylesheet&gt;&lt;/head&gt;&lt;body&gt;&lt;noscript&gt;&lt;strong&gt;We're sorry but fe doesn't work properly without JavaScript enabled. Please enable it to continue.&lt;/strong&gt;&lt;/noscript&gt;&lt;div id=app&gt;&lt;/div&gt;&lt;script src=/js/chunk-vendors.14b9b088.js&gt;&lt;/script&gt;&lt;script src=/js/app.ee469174.js&gt;&lt;/script&gt;&lt;/body&gt;&lt;/html&gt;
</code></pre>
<p>服务可以正常访问。</p>
<h2>总结</h2>
<p>通过本节我们学习到了 <code>chart</code> 的实际结构，及编写方式。以及编写了我们自己的 <code>chart</code> 并使用该 <code>chart</code> 部署了服务。</p>
<p>示例项目还仅仅是个小项目，试想当我们需要部署一个大型项目，如果不通过类似 Helm 这样的软件进行管理，每次的更新发布，维护 <code>YAML</code> 的配置文件就会很繁琐了。</p>
<p>另外，Helm 的功能还不仅限于此，使用 Helm 我们还可以管理 <code>Release</code> ，并进行更新回滚等操作。以及，我们可以搭建自己的私有 <code>chart</code> 仓库等。</p>
<p>下节开始，我们将进入深入学习阶段，逐个讲解 K8S 的核心组件，以便后续遇到问题时，可快速定位和解决。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="10&#32;应用管理：初识&#32;Helm.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="12&#32;庖丁解牛：kube-apiserver.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345fb0a5570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
