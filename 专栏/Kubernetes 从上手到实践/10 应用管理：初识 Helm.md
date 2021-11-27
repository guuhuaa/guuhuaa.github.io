<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>10 应用管理：初识 Helm.md</title>
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

                    <a class="current-tab" href="10&#32;应用管理：初识&#32;Helm.md">10 应用管理：初识 Helm.md</a>
                    

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
                        <div><h1>10 应用管理：初识 Helm</h1>
<h2>整体概览</h2>
<p>上节，我们已经学习了如何通过编写配置文件的方式部署项目。而在实际生产环境中，项目所包含组件可能不止 3 个，并且可能项目数会很多，如果每个项目的发布，更新等都通过手动去编写配置文件的方式，实在不利于管理。</p>
<p>并且，当线上出现个别组件升级回滚之类的操作，如果组件之间有相关版本依赖等情况，那事情会变得复杂的多。我们需要有更简单的机制来辅助我们完成这些事情。</p>
<h2>Helm 介绍</h2>
<p><a href="https://www.helm.sh/">Helm</a> 是构建于 K8S 之上的包管理器，可与我们平时接触到的 <code>Yum</code>，<code>APT</code>，<code>Homebrew</code> 或者 <code>Pip</code> 等包管理器相类比。</p>
<p>使用 Helm 可简化包分发，安装，版本管理等操作流程。同时它也是 CNCF 孵化项目。</p>
<h2>Helm 安装</h2>
<p>Helm 是 C/S 架构，主要分为客户端 <code>helm</code> 和服务端 <code>Tiller</code>。安装时可直接在 <a href="https://github.com/helm/helm/releases">Helm 仓库的 Release 页面</a> 下载所需二进制文件或者源码包。</p>
<p>由于当前项目的二进制文件存储已切换为 GCS，我已经为国内用户准备了最新版本的二进制包，可通过以下链接进行下载。</p>
<pre><code>链接: https://pan.baidu.com/s/1n1zj3rlv2NyfiA6kRGrHfg 提取码: 5huw 
</code></pre>
<p>下载后对文件进行解压，我这里以 Linux amd64 为例。</p>
<pre><code>➜  /tmp tar -zxvf helm-v2.11.0-linux-amd64.tar.gz
linux-amd64/
linux-amd64/tiller
linux-amd64/README.md
linux-amd64/helm
linux-amd64/LICENSE
➜  /tmp tree linux-amd64 
linux-amd64
├── helm
├── LICENSE
├── README.md
└── tiller

0 directories, 4 files
</code></pre>
<p>解压完成后，可看到其中包含 <code>helm</code> 和 <code>tiller</code> 二进制文件。</p>
<h3>客户端 helm</h3>
<p><code>helm</code> 是个二进制文件，直接将它移动至 <code>/usr/bin</code> 目录下即可。</p>
<pre><code>➜  /tmp sudo mv linux-amd64/helm /usr/bin/helm 
</code></pre>
<p>这时候便可直接通过 <code>helm</code> 命令使用了。比如，我们验证当前使用的版本。</p>
<pre><code>➜  /tmp helm version
Client: &amp;version.Version{SemVer:&quot;v2.11.0&quot;, GitCommit:&quot;2e55dbe1fdb5fdb96b75ff144a339489417b146b&quot;, GitTreeState:&quot;clean&quot;}
Error: Get http://localhost:8080/api/v1/namespaces/kube-system/pods?labelSelector=app%3Dhelm%2Cname%3Dtiller: dial tcp 127.0.0.1:8080: connect: connection refused
</code></pre>
<p>可以看到上面有明显的报错，并且很像 <code>kubectl</code> 未正确配置时的错误。这是因为 <code>helm</code> 默认会去读取 <code>$HOME/.kube/config</code> 的配置文件，用于正确的连接至目标集群。</p>
<p>当我们正确的配置好 <code>$HOME/.kube/config</code> 文件时，再次执行：</p>
<pre><code>➜  /tmp helm version
Client: &amp;version.Version{SemVer:&quot;v2.11.0&quot;, GitCommit:&quot;2e55dbe1fdb5fdb96b75ff144a339489417b146b&quot;, GitTreeState:&quot;clean&quot;}
Error: could not find tiller
</code></pre>
<p>这次报错是因为找不到服务端 <code>Tiller</code>，接下来我们部署服务端。</p>
<h3>服务端 Tiller</h3>
<p>以下讨论中，前提都是 <code>$HOME/.kube/config</code> 已正确配置，并且 <code>kebectl</code> 有操作集群的权限。</p>
<h4>本地安装</h4>
<p>刚才我们解压的文件中，还有一个二进制文件 <code>tiller</code> 。我们可以直接执行它，用于在本地启动服务。</p>
<pre><code>➜  /tmp ./linux-amd64/tiller
[main] 2018/11/18 23:47:10 Starting Tiller v2.11.0 (tls=false)
[main] 2018/11/18 23:47:10 GRPC listening on :44134
[main] 2018/11/18 23:47:10 Probes listening on :44135
[main] 2018/11/18 23:47:10 Storage driver is ConfigMap
[main] 2018/11/18 23:47:10 Max history per release is 0
</code></pre>
<p>直接执行时，默认会监听 <code>44134</code> 和 <code>44135</code> 端口，<code>44134</code> 端口用于和 <code>helm</code> 进行通信，而 <code>44135</code> 主要是用于做探活的，在部署至 K8S 时使用。</p>
<p>当我们使用客户端连接时，只需设置 <code>HELM_HOST</code> 环境变量即可。</p>
<pre><code>➜  ~ export HELM_HOST=localhost:44134
➜  ~ helm version
Client: &amp;version.Version{SemVer:&quot;v2.11.0&quot;, GitCommit:&quot;2e55dbe1fdb5fdb96b75ff144a339489417b146b&quot;, GitTreeState:&quot;clean&quot;}
Server: &amp;version.Version{SemVer:&quot;v2.11.0&quot;, GitCommit:&quot;2e55dbe1fdb5fdb96b75ff144a339489417b146b&quot;, GitTreeState:&quot;clean&quot;}
</code></pre>
<p><strong>注意</strong> 一定要正确配置 <code>$HOME/.kube/config</code> 文件，否则会影响正常功能使用。</p>
<h4>默认安装</h4>
<p>官方提供了一种一键式安装的方式。那便是 <code>helm init</code> 执行这条命令后，会同时在 K8S 中部署服务端 Tiller 和初始化 helm 的默认目录 <code>$HELM_HOME</code> 默认值为 <code>$HOME/.helm</code>。</p>
<p>这种方式下会默认使用官方镜像 <code>gcr.io/kubernetes-helm/tiller</code> 网络原因可能会导致安装失败。所以我已将官方镜像进行同步。可使用以下方式进行使用：</p>
<pre><code>➜  ~ helm init --tiller-image taobeier/tiller:v2.11.0 
Creating /root/.helm
Creating /root/.helm/repository
Creating /root/.helm/repository/cache
Creating /root/.helm/repository/local
Creating /root/.helm/plugins
Creating /root/.helm/starters
Creating /root/.helm/cache/archive
Creating /root/.helm/repository/repositories.yaml
Adding stable repo with URL: https://kubernetes-charts.storage.googleapis.com
Adding local repo with URL: http://127.0.0.1:8879/charts
$HELM_HOME has been configured at /root/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
To prevent this, run `helm init` with the --tiller-tls-verify flag.
For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
Happy Helming!
➜  ~ helm version
Client: &amp;version.Version{SemVer:&quot;v2.11.0&quot;, GitCommit:&quot;9ad53aac42165a5fadc6c87be0dea6b115f93090&quot;, GitTreeState:&quot;clean&quot;}
Server: &amp;version.Version{SemVer:&quot;v2.11.0&quot;, GitCommit:&quot;2e55dbe1fdb5fdb96b75ff144a339489417b146b&quot;, GitTreeState:&quot;clean&quot;}
</code></pre>
<p>可以看到 <code>$HELM_HOME</code> 目录已经初始化完成，客户端与服务端已可以正常通信。查看下当前 K8S 集群中的情况：</p>
<pre><code>➜  ~ kubectl -n kube-system get deploy tiller-deploy
NAME            DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
tiller-deploy   1         1         1            1           6m
</code></pre>
<p>可以看到已正常部署。</p>
<h4>手动安装</h4>
<p>通过上面的描述，可能你已经发现，安装服务端，其实也就是一次普通的部署，我们可以通过以下方式来自行通过 <code>kubectl</code> 完成部署。</p>
<pre><code>➜  ~ helm init --dry-run --debug  # 篇幅原因，以下内容进行了省略
---                               
apiVersion: extensions/v1beta1
kind: Deployment                                    
metadata:                            
  creationTimestamp: null
  labels:         
    app: helm              
    name: tiller       
  name: tiller-deploy           
  namespace: kube-system   
spec:               
  replicas: 1 
  strategy: {}                
  ...
status: {}

---
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  labels:
    app: helm
    name: tiller
  name: tiller-deploy
  namespace: kube-system
spec:
  ports:
  - name: tiller
    port: 44134
    targetPort: tiller
  selector:
    app: helm
    name: tiller
  type: ClusterIP
status:
  loadBalancer: {}
</code></pre>
<p>将输出内容保存至文件中，自行修改后，通过 <code>kubectl</code> 进行部署即可。建议在修改过程中，尽量不要去更改标签及选择器。</p>
<h4>RBAC 使用</h4>
<p>上面的内容中，均未提及到权限控制相关的内容，但是在生产环境中使用，我们一般都是会进行权限控制的。</p>
<p>在第 8 节中，我们已经详细的解释了认证授权相关的内容。所以下面的内容不做太多详细解释。</p>
<p>这里我们创建一个 <code>ServiceAccount</code> 命名为 <code>tiller</code>，为了简单，我们直接将它与 <code>cluster-admin</code> 进行绑定。</p>
<pre><code>apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system
</code></pre>
<p>将此内容保存为 <code>tiller-rbac.yaml</code>，开始进行部署操作。</p>
<pre><code>➜  ~ kubectl apply -f tiller-rbac.yaml
serviceaccount/tiller created
clusterrolebinding.rbac.authorization.k8s.io/tiller created
➜  ~ helm init --service-account tiller
Creating /root/.helm
Creating /root/.helm/repository
Creating /root/.helm/repository/cache
Creating /root/.helm/repository/local
Creating /root/.helm/plugins
Creating /root/.helm/starters
Creating /root/.helm/cache/archive
Creating /root/.helm/repository/repositories.yaml
Adding stable repo with URL: https://kubernetes-charts.storage.googleapis.com
Adding local repo with URL: http://127.0.0.1:8879/charts
$HELM_HOME has been configured at /root/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
To prevent this, run `helm init` with the --tiller-tls-verify flag.
For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
Happy Helming!
➜  ~ helm version
Client: &amp;version.Version{SemVer:&quot;v2.11.0&quot;, GitCommit:&quot;2e55dbe1fdb5fdb96b75ff144a339489417b146b&quot;, GitTreeState:&quot;clean&quot;}
Server: &amp;version.Version{SemVer:&quot;v2.11.0&quot;, GitCommit:&quot;2e55dbe1fdb5fdb96b75ff144a339489417b146b&quot;, GitTreeState:&quot;clean&quot;}
</code></pre>
<p>以此方式完成部署。</p>
<h2>Helm 概念</h2>
<h3>Chart</h3>
<p><code>chart</code> 就是 Helm 所管理的包，类似于 <code>Yum</code> 所管理的 <code>rpm</code> 包或是 <code>Homebrew</code> 管理的 <code>Formulae</code>。它包含着一个应用要部署至 K8S 上所必须的所有资源。</p>
<h3>Release</h3>
<p><code>Release</code> 就是 <code>chart</code> 在 K8S 上部署后的实例。<code>chart</code> 的每次部署都将产生一次 <code>Release</code>。这和上面类比的包管理器就有所不同了，多数的系统级包管理器所安装的包只会在系统中存在一份。我们可以以 <code>Pip</code> 在虚拟环境下的包安装，或者 <code>Npm</code> 的 local install 来进行类比。</p>
<h3>Repository</h3>
<p><code>Repository</code> 就是字面意思，存储 <code>chart</code> 的仓库。还记得我们上面执行 <code>helm init</code> 时的输出吗？默认情况下，初始化 Helm 的时候，会添加两个仓库，一个是 <code>stable</code> 仓库 <a href="https://kubernetes-charts.storage.googleapis.com/">kubernetes-charts.storage.googleapis.com</a> 另一个则是 <code>local</code> 仓库，地址是 <a href="http://127.0.0.1:8879/charts">http://127.0.0.1:8879/charts</a> 。</p>
<h3>Config</h3>
<p>前面提到了 <code>chart</code> 是应用程序所必须的资源，当然我们实际部署的时候，可能就需要有些自定义的配置了。<code>Config</code> 便是用于完成此项功能的，在部署时候，会将 <code>config</code> 与 <code>chart</code> 进行合并，共同构成我们将部署的应用。</p>
<h2>Helm 的工作原理</h2>
<p><code>helm</code> 通过 <code>gRPC</code> 将 <code>chart</code> 发送至 <code>Tiller</code> ，<code>Tiller</code> 则通过内置的 <code>kubernetes</code> 客户端库与 K8S 的 API server 进行交流，将 <code>chart</code> 进行部署，并生成 <code>Release</code> 用于管理。</p>
<p>前面只说到了 <code>helm</code> 与 <code>Tiller</code> 交互的协议，但尚未说其数据链路。</p>
<p>我们来看看 <code>Tiller</code> 的部署情况。主要看 <code>Service</code>：</p>
<pre><code>➜  ~ kubectl -n kube-system get svc
NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)         AGE
kube-dns        ClusterIP   10.96.0.10       &lt;none&gt;        53/UDP,53/TCP   1h
tiller-deploy   ClusterIP   10.107.204.164   &lt;none&gt;        44134/TCP       33m
</code></pre>
<p><code>Tiller</code> 默认采用 <code>ClusterIP</code> 类型的 <code>Service</code> 进行部署。而我们知道的 <code>ClusterIP</code> 类型的 <code>Service</code> 是仅限集群内访问的。</p>
<p>在这里所依赖的技术，便是在第 5 节，我们提到的 <code>socat</code> 。<code>helm</code> 通过 <code>socat</code> 的端口转发（或者说 K8S 的代理），进而实现了本地与 <code>Tiller</code> 的通信。</p>
<p>当然，以上内容均以当前最新版本 <code>2.11.0</code> 为例。当下一个大版本 Helm v3 出现时， <code>Tiller</code> 将不复存在，通信机制和工作原理也将发生变化。</p>
<h2>总结</h2>
<p>通过本节，我们已经学习到了 Helm 的基础知识和工作原理，了解到了 Helm 的用途以及如何在本地和 K8S 中部署它。需要注意的是 <code>$HOME/.kube/config</code> 需要提前配置好，以及 <code>socat</code> 工具需要提前安装，可参考第 5 节的内容。</p>
<p>接下来，我们将上节中的示例项目使用 Helm 部署至 K8S 集群中。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="09&#32;应用发布：部署实际项目.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="11&#32;部署实践：以&#32;Helm&#32;部署项目.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345f5acf370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
