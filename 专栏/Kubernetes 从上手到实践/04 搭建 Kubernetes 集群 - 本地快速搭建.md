<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>04 搭建 Kubernetes 集群 - 本地快速搭建.md</title>
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

                    <a class="current-tab" href="04&#32;搭建&#32;Kubernetes&#32;集群&#32;-&#32;本地快速搭建.md">04 搭建 Kubernetes 集群 - 本地快速搭建.md</a>
                    

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
                        <div><h1>04 搭建 Kubernetes 集群 - 本地快速搭建</h1>
<p>通过之前的学习，我们已经知道了 K8S 中有一些组件是必须的，集群中有不同的角色。本节，我们在本地快速搭建一个集群，以加深我们学习到的东西。</p>
<h2>方案选择</h2>
<p>在上一节中，我们知道 K8S 中有多种功能组件，而这些组件要在本地全部搭建好，需要一些基础知识，以及在搭建过程中会浪费不少的时间，从而可能会影响我们正常的搭建集群的目标。</p>
<p>所以，我们这里提供两个最简单，最容易实现我们目标的工具</p>
<ul>
<li><a href="https://github.com/kubernetes-sigs/kind/">KIND</a> 。</li>
<li><a href="https://github.com/kubernetes/minikube">Minikube</a> 。</li>
</ul>
<h2>KIND</h2>
<h3>介绍</h3>
<p>KIND（Kubernetes in Docker）是为了能提供更加简单，高效的方式来启动 K8S 集群，目前主要用于比如 <code>Kubernetes</code> 自身的 CI 环境中。</p>
<h3>安装</h3>
<ul>
<li>可以直接在项目的 <a href="https://github.com/kubernetes-sigs/kind/releases">Release 页面</a> 下载已经编译好的二进制文件。(下文中使用的是 v0.1.0 版本的二进制包)</li>
</ul>
<p>注意：如果不直接使用二进制包，而是使用 <code>go get sigs.k8s.io/kind</code> 的方式下载，则与下文中的配置文件不兼容。<strong>请参考使用 Kind 搭建你的本地 Kubernetes 集群</strong> 这篇文章。</p>
<p>更新（2020年2月5日）：KIND 已经发布了 v0.7.0 版本，如果你想使用新版本，建议参考 <a href="https://zhuanlan.zhihu.com/p/105173589">使用 Kind 在离线环境创建 K8S 集群</a> ，这篇文章使用了最新版本的 KIND。</p>
<p><img src="assets/16898b9e3d57fcab" alt="img" /></p>
<h3>创建集群</h3>
<p><strong>在使用 KIND 之前，你需要本地先安装好 Docker 的环境</strong> ，此处暂不做展开。</p>
<p>由于网络问题，我们此处也需要写一个配置文件，以便让 <code>kind</code> 可以使用国内的镜像源。（KIND 最新版本中已经内置了所有需要的镜像，无需此操作）</p>
<pre><code>apiVersion: kind.sigs.k8s.io/v1alpha1
kind: Config

kubeadmConfigPatches:
- |
  apiVersion: kubeadm.k8s.io/v1alpha3
  kind: InitConfiguration
  nodeRegistration:
  kubeletExtraArgs:
    pod-infra-container-image: registry.aliyuncs.com/google_containers/pause-amd64:3.1
- |
  apiVersion: kubeadm.k8s.io/v1alpha3
  kind: ClusterConfiguration
  imageRepository: registry.aliyuncs.com/google_containers
  kubernetesVersion: v1.12.2
  networking:
    serviceSubnet: 10.0.0.0/16
</code></pre>
<p>将上面的内容保存成 <code>kind-config.yaml</code> 文件，执行以下命令即可。</p>
<pre><code>kind create cluster --image kindest/node:v1.12.2 --config kind-config.yaml --name moelove                  
</code></pre>
<p>下面为在我机器上执行的程序输出：</p>
<pre><code>(MoeLove) ➜  kind ✗ kind create cluster --image kindest/node:v1.12.2 --config kind-config.yaml --name moelove                  
Creating cluster 'kind-moelove' ...
 ✓ Ensuring node image (kindest/node:v1.12.2) 🖼
 ✓ [kind-moelove-control-plane] Creating node container 📦                                                         
 ✓ [kind-moelove-control-plane] Fixing mounts 🗻
 ✓ [kind-moelove-control-plane] Starting systemd 🖥
 ✓ [kind-moelove-control-plane] Waiting for docker to be ready 🐋                                                  
 ✓ [kind-moelove-control-plane] Starting Kubernetes (this may take a minute) ☸                                     
Cluster creation complete. You can now use the cluster with:

export KUBECONFIG=&quot;$(kind get kubeconfig-path --name=&quot;moelove&quot;)&quot;
kubectl cluster-info
</code></pre>
<p>这里，通过传递上面的 <code>kind-config.yaml</code> 文件给 <code>kind create cluster</code>, 并传递了一个名字通过 <code>--name</code> 参数。</p>
<p>我们按照程序输出的提示进行操作：</p>
<pre><code>export KUBECONFIG=&quot;$(kind get kubeconfig-path --name=&quot;moelove&quot;)&quot;
kubectl cluster-info
</code></pre>
<p>下面为在我机器上执行的程序输出：</p>
<pre><code>(MoeLove) ➜  kind ✗ export KUBECONFIG=&quot;$(kind get kubeconfig-path --name=&quot;moelove&quot;)&quot;
(MoeLove) ➜  kind ✗ kubectl cluster-info
Kubernetes master is running at https://localhost:35911
KubeDNS is running at https://localhost:35911/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
(MoeLove) ➜  kind ✗ kubectl version
Client Version: version.Info{Major:&quot;1&quot;, Minor:&quot;11&quot;, GitVersion:&quot;v1.11.3&quot;, GitCommit:&quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-09-09T18:02:47Z&quot;, GoVersion:&quot;go1.10.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
Server Version: version.Info{Major:&quot;1&quot;, Minor:&quot;12&quot;, GitVersion:&quot;v1.12.2&quot;, GitCommit:&quot;17c77c7898218073f14c8d573582e8d2313dc740&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-10-24T06:43:59Z&quot;, GoVersion:&quot;go1.10.4&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
</code></pre>
<p>注意，这里需要安装 <code>kubectl</code>。 <code>kubectl</code> 的安装可参考下面的内容。</p>
<p>当你执行 <code>kubectl cluster-info</code> 如果可以看到类似我上面的输出，那你本地的 K8S 集群就已经部署好了。你可以直接阅读第 5 节或者第 6 节的内容。</p>
<p>如果你已经对 K8S 有所了解，并且对 Dashboard 有比较强烈需求的话, 可直接参考第 20 节的内容。</p>
<h2>Minikube</h2>
<h3>介绍</h3>
<p>Minikube 是 K8S 官方为了开发者能在个人电脑上运行 K8S 而提供的一套工具。实现上是通过 Go 语言编写，通过调用虚拟化管理程序，创建出一个运行在虚拟机内的单节点集群。</p>
<p>注：从这里也可以看出，对于 K8S 集群的基本功能而言，节点数并没有什么限制。只有一个节点同样可以创建集群。</p>
<h3>前期准备</h3>
<ul>
<li>首先需要确认 BIOS 已经开启了 <code>VT-x</code> 或者 <code>AMD-v</code> 虚拟化的支持。具体方式可参考 <a href="https://www.shaileshjha.com/how-to-find-out-if-intel-vt-x-or-amd-v-virtualization-technology-is-supported-in-windows-10-windows-8-windows-vista-or-windows-7-machine/">确认是否已开启 BIOS 虚拟化</a>, <a href="https://www.howtogeek.com/213795/how-to-enable-intel-vt-x-in-your-computers-bios-or-uefi-firmware/">开启 BIOS 虚拟化支持</a> 这两篇文章。</li>
<li>其次我们需要安装一个虚拟化管理程序，这里的选择可根据你实际在用的操作系统来决定。官方推荐如下:
<ul>
<li>macOS: <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox</a> 或 <a href="https://www.vmware.com/products/fusion">VMware Fusion</a> 或 <a href="https://github.com/moby/hyperkit">HyperKit</a>。如果使用 Hyperkit 需要注意系统必须是 <code>OS X 10.10.3 Yosemite</code> 及之后版本的。</li>
<li>Linux: <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox</a> 或 <a href="http://www.linux-kvm.org/">KVM</a>。</li>
<li>Windows: <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox</a> 或 <a href="https://msdn.microsoft.com/en-us/virtualization/hyperv_on_windows/quick_start/walkthrough_install">Hyper-V</a>。</li>
</ul>
</li>
</ul>
<p>我个人推荐无论你在以上哪种操作系统中使用 Minikube 都选择用 <code>Virtualbox</code> 作为虚拟化管理程序，1. Virtualbox 无论操作体验还是安装都比较简单 2. Minikube 对其支持更完备，并且也已经经过大量用户测试，相关问题均已基本修复。</p>
<p><em>如果你是在 Linux 系统上面，其实还有一个选择，便是将 Minikube 的 --vm-driver 参数设置为 none ，并且在本机已经正确安装 Docker。 这种方式是无需虚拟化支持的。</em></p>
<h3>安装 kubectl</h3>
<p>上一节我们已经学到 K8S 集群是典型的 C/S 架构，有一个官方提供的名为 <code>kubectl</code> 的 CLI 工具。在这里，我们要安装 <code>kubectl</code> 以便后续我们可以对搭建好的集群进行管理。</p>
<p><strong>注：由于 API 版本兼容的问题，尽量保持 kubectl 版本与 K8S 集群版本保持一致，或版本相差在在一个小版本内。</strong></p>
<p>官方文档提供了 <code>macOS</code>, <code>Linux</code>, <code>Windows</code> 等操作系统上的安装方式，且描述很详细，这里不过多赘述，<a href="https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl">文档地址</a>。</p>
<p><strong>此处提供一个不同于官方文档中的安装方式。</strong></p>
<ul>
<li>访问 K8S 主仓库的 <a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG.md">CHANGELOG 文件</a> 找到你所需要的版本。 由于我们将要使用的 Minikube 是官方最新的稳定版 v0.28.2，而它内置的 Kubernetes 的版本是 v1.10 所以，我们选择使用对应的 <a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.10.md">1.10 版本</a>的 <code>kubectl</code>。当然，我们也可以通过传递参数的方式来创建不同版本的集群。如 <code>minikube start --kubernetes-version v1.11.3</code> 用此命令创建 <code>v1.11.3</code> 版本的集群，当然 <code>kubectl</code> 的版本也需要相应升级。</li>
</ul>
<p><img src="assets/165d772ecb0454f6" alt="img" /></p>
<p>点击<a href="https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG-1.10.md#client-binaries">Client Binaries</a> 找到你符合所需系统架构的对应包下载即可。这里我以 <a href="https://dl.k8s.io/v1.10.7/kubernetes-client-linux-amd64.tar.gz">Linux 下 64 位的包</a>为例。</p>
<pre><code>➜  wget https://dl.k8s.io/v1.10.7/kubernetes-client-linux-amd64.tar.gz
➜  echo '169b57c6707ed8d8be9643b0088631e5c0c6a37a5e99205f03c1199cd32bc61e  kubernetes-client-linux-amd64.tar.gz' | sha256sum -c -
kubernetes-client-linux-amd64.tar.gz: 成功
➜  tar zxf kubernetes-client-linux-amd64.tar.gz
➜  sudo mv kubernetes/client/bin/kubectl /usr/local/bin/kubectl
➜  /usr/local/bin/kubectl version --client
Client Version: version.Info{Major:&quot;1&quot;, Minor:&quot;10&quot;, GitVersion:&quot;v1.10.7&quot;, GitCommit:&quot;0c38c362511b20a098d7cd855f1314dad92c2780&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-08-20T10:09:03Z&quot;, GoVersion:&quot;go1.9.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
</code></pre>
<p>执行以上命令即可完成 <code>kubectl</code> 的安装，最后一步会看到当前安装的版本信息等。</p>
<h3>安装 Minikube</h3>
<p>先查看 Minikube 的 <a href="https://github.com/kubernetes/minikube/releases">Release 页面</a>，当前最新的稳定版本是 v0.28.2，找到你所需系统的版本，点击下载，并将下载好的可执行文件加入你的 PATH 中。</p>
<p><img src="assets/165d772a6493a287" alt="img" /></p>
<p><strong>注：当前 Windows 系统下的安装包还处于实验性质，如果你是在 Windows 环境下，同样是可以下载安装使用的</strong></p>
<p>以 Linux 下的安装为例：</p>
<pre><code>➜  wget -O minikube https://github.com/kubernetes/minikube/releases/download/v0.28.2/minikube-linux-amd64
➜  chmod +x minikube
➜  sudo mv minikube /usr/local/bin/minikube

➜  /usr/local/bin/minikube version
minikube version: v0.28.2
</code></pre>
<p>最后一步可查看当前已安装好的 Minikube 的版本信息。如果安装成功将会看到和我上面内容相同的结果。</p>
<h3>创建第一个 K8S 集群</h3>
<p>使用 Minikube 创建集群，只要简单的执行 <code>minikube start</code> 即可。正常情况下，你会看到和我类似的输出。</p>
<pre><code>➜  ~ minikube start
Starting local Kubernetes v1.10.0 cluster...
Starting VM...
Getting VM IP address...
Moving files into cluster...
Setting up certs...
Connecting to cluster...
Setting up kubeconfig...
Starting cluster components...
Kubectl is now configured to use the cluster.
Loading cached images from config file.

➜  ~ minikube status
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100         
</code></pre>
<p>为了验证我们的集群目前是否均已配置正确，可以执行以下命令查看。</p>
<pre><code>➜  ~ kubectl cluster-info 
Kubernetes master is running at https://192.168.99.100:8443
KubeDNS is running at https://192.168.99.100:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

➜  ~ kubectl get nodes
NAME       STATUS    ROLES     AGE       VERSION
minikube   Ready     master    1d       v1.10.0
</code></pre>
<p>如果出现类似拒绝连接之类的提示，那可能是因为你的 <code>kubectl</code> 配置不正确，可查看 <code>$HOME/.kube/config</code> 文件检查配置。示例输出如下：</p>
<pre><code>➜  ~ cat .kube/config
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/tao/.minikube/ca.crt
    server: https://192.168.99.100:8443
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
<p>如果没有该文件，可按上面示例内容进行创建，替换掉其中的路径及 <code>server</code> 地址配置。 <code>server</code> 地址可通过 <code>minikube status</code> 或者 <code>minikube ip</code> 查看或检查。</p>
<pre><code>(Tao) ➜  ~ minikube ip
192.168.99.100

(Tao) ➜  ~ minikube status
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100
</code></pre>
<h3>通过 Dashboard 查看集群当前状态</h3>
<p>使用 <code>Minikube</code> 的另一个好处在于，你可以不用关注太多安装方面的过程，直接在终端下输入 <code>minikube dashboard</code> 打开系统 Dashboard 并通过此来查看集群相关状态。</p>
<p>执行 <code>minikube dashboard</code> 后会自动打开浏览器，默认情况下监听在通过 <code>minikube ip</code> 所获得 IP 的 3000 端口。如下图所示：</p>
<p><img src="assets/165de25c7c517d78" alt="img" /></p>
<h3>相关链接:</h3>
<ul>
<li><a href="https://websiteforstudents.com/installing-virtualbox-ubuntu-17-04/">安装 VirtualBox</a></li>
<li><a href="https://juejin.im/post/6844903807562989582">使用 Kind 搭建你的本地 Kubernetes 集群</a></li>
</ul>
<h2>总结</h2>
<p>本节中，我们为了能更快的体验到 K8S 集群，避免很多繁琐的安装步骤，我们选择了使用官方提供的 <code>Minikube</code> 工具来搭建一个本地集群。</p>
<p>Minikube 的本质其实是将一套 “定制化” 的 K8S 集群打包成 ISO 镜像，当执行 <code>minikube start</code> 的时候，便通过此镜像启动一个虚拟机，在此虚拟机上通过 <code>kubeadm</code> 工具来搭建一套只有一个节点的 K8S 集群。关于 <code>kubeadm</code> 工具，我们在下节进行讲解。</p>
<p>同时，会通过虚拟机的相关配置接口拿到刚才所启动虚拟机的地址信息等，并完成本地的 <code>kubectl</code> 工具的配置，以便于让用户通过 <code>kubectl</code> 工具对集群进行操作。</p>
<p>事实上，当前 Docker for Mac 17.12 CE Edge 和 Docker for Windows 18.02 CE Edge ，以及这两种平台更高的 Edge 版本, 均已内置了对 K8S 的支持，但均为 Edge 版本，此处暂不做过多介绍。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="03&#32;宏观认识：整体架构.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="05&#32;动手实践：搭建一个&#32;Kubernetes&#32;集群&#32;-&#32;生产可用.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4345d22f7770ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
