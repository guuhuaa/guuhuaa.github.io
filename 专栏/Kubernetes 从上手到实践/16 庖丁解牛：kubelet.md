<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16 庖丁解牛：kubelet.md</title>
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

                    <a class="current-tab" href="16&#32;庖丁解牛：kubelet.md">16 庖丁解牛：kubelet.md</a>
                    

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
                        <div><h1>16 庖丁解牛：kubelet</h1>
<h2>整体概览</h2>
<pre><code>+--------------------------------------------------------+       
| +---------------------+        +---------------------+ |       
| |      kubelet        |        |     kube-proxy      | |       
| |                     |        |                     | |       
| +---------------------+        +---------------------+ |       
| +----------------------------------------------------+ |       
| | Container Runtime (Docker)                         | |       
| | +---------------------+    +---------------------+ | |       
| | |Pod                  |    |Pod                  | | |       
| | | +-----+ +-----+     |    |+-----++-----++-----+| | |       
| | | |C1   | |C2   |     |    ||C1   ||C2   ||C3   || | |       
| | | |     | |     |     |    ||     ||     ||     || | |       
| | | +-----+ +-----+     |    |+-----++-----++-----+| | |       
| | +---------------------+    +---------------------+ | |       
| +----------------------------------------------------+ |       
+--------------------------------------------------------+  
</code></pre>
<p>在第 3 节《宏观认识：整体架构》 中，我们知道了 K8S 中 Node 由一些必要的组件构成，而其中最为核心的当属 <code>kubelet</code> 了，如果没有 <code>kubelet</code> 的存在，那我们预期的各类资源就只能存在于 <code>Master</code> 的相关组件中了，而 K8S 也很能只是一个 CRUD 的普通程序了。本节，我们来介绍下 <code>kubelet</code> 及它是如何完成这一系列任务的。</p>
<h2><code>kubelet</code> 是什么</h2>
<p>按照一般架构设计上的习惯，<code>kubelet</code> 所承担的角色一般会被叫做 <code>agent</code>，这里叫做 <code>kubelet</code> 很大程度上受 <code>Borg</code> 的命名影响，<code>Borg</code> 里面也有一个 <code>Borglet</code> 的组件存在。<code>kubelet</code> 便是 K8S 中的 <code>agent</code>，负责 <code>Node</code> 和 <code>Pod</code> 相关的管理任务。</p>
<p>同样的，在我们下载 K8S 二进制文件解压后，便可以得到 <code>kubelet</code> 的可执行文件。在第 5 节中，我们也完成了 <code>kubelet</code> 以 <code>systemd</code> 进行启动和管理的相关配置。</p>
<h2><code>kubelet</code> 有什么作用</h2>
<p>通常来讲 <code>agent</code> 这样的角色起到的作用首先便是要能够注册，让 <code>server</code> 端知道它的存在，所以这便是它的第一个作用：节点管理。</p>
<h3>节点管理</h3>
<p>当我们执行 <code>kubelet --help</code> 的时候，会看到它所支持的可配置参数，其中有一个 <code>--register-node</code> 参数便是用于控制是否向 <code>kube-apiserver</code> 注册节点的，默认是开启的。</p>
<p>我们在第 5 节中还介绍了如何新增一个 <code>Node</code>，当 <code>kubeadm join</code> 执行成功后，你便可以通过 <code>kubectl get node</code> 查看到新加入集群中的 <code>Node</code>，与此同时，你也可以在该节点上通过以下命令查看 <code>kubelet</code> 的状态。</p>
<pre><code>master $ systemctl status kubelet
● kubelet.service - kubelet: The Kubernetes Agent
   Loaded: loaded (/etc/systemd/system/kubelet.service; enabled; vendor preset: disabled)
  Drop-In: /etc/systemd/system/kubelet.service.d
           └─kubeadm.conf
   Active: active (running) since Thu 2018-12-13 07:49:51 UTC; 32min ago
     Docs: http://kubernetes.io/docs/
 Main PID: 3876259 (kubelet)
   Memory: 66.3M
   CGroup: /system.slice/kubelet.service
           └─3876259 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernete...
</code></pre>
<p>当我们查看 <code>Node</code> 信息时，也能得到如下输出：</p>
<pre><code>master $ kubectl get nodes node01 -o yaml
apiVersion: v1
kind: Node
metadata:
  annotations:
    kubeadm.alpha.kubernetes.io/cri-socket: /var/run/dockershim.sock
    node.alpha.kubernetes.io/ttl: &quot;0&quot;
    volumes.kubernetes.io/controller-managed-attach-detach: &quot;true&quot;
  creationTimestamp: 2018-12-13T07:50:47Z
  labels:
    beta.kubernetes.io/arch: amd64
    beta.kubernetes.io/os: linux
    kubernetes.io/hostname: node01
  name: node01
  resourceVersion: &quot;4242&quot;
  selfLink: /api/v1/nodes/node01
  uid: cd612df6-feab-11e8-9a0b-0242ac110096
spec: {}
status:
  addresses:
  - address: 172.17.0.152
    type: InternalIP
  - address: node01
    type: Hostname
  allocatable:
    cpu: &quot;4&quot;
    ephemeral-storage: &quot;89032026784&quot;
    hugepages-1Gi: &quot;0&quot;
    hugepages-2Mi: &quot;0&quot;
    memory: 3894788Ki
    pods: &quot;110&quot;
  capacity:
    cpu: &quot;4&quot;
    ephemeral-storage: 96605932Ki
    hugepages-1Gi: &quot;0&quot;
    hugepages-2Mi: &quot;0&quot;
    memory: 3997188Ki
    pods: &quot;110&quot;
  conditions:
  - lastHeartbeatTime: 2018-12-13T08:39:41Z
    lastTransitionTime: 2018-12-13T07:50:47Z
    message: kubelet has sufficient disk space available
    reason: KubeletHasSufficientDisk
    status: &quot;False&quot;
    type: OutOfDisk
  - lastHeartbeatTime: 2018-12-13T08:39:41Z
    lastTransitionTime: 2018-12-13T07:50:47Z
    message: kubelet has sufficient memory available
    reason: KubeletHasSufficientMemory
    status: &quot;False&quot;
    type: MemoryPressure
  - lastHeartbeatTime: 2018-12-13T08:39:41Z
    lastTransitionTime: 2018-12-13T07:50:47Z
    message: kubelet has no disk pressure
    reason: KubeletHasNoDiskPressure
    status: &quot;False&quot;
    type: DiskPressure
  - lastHeartbeatTime: 2018-12-13T08:39:41Z
    lastTransitionTime: 2018-12-13T07:50:47Z
    message: kubelet has sufficient PID available
    reason: KubeletHasSufficientPID
    status: &quot;False&quot;
    type: PIDPressure
  - lastHeartbeatTime: 2018-12-13T08:39:41Z
    lastTransitionTime: 2018-12-13T07:51:37Z
    message: kubelet is posting ready status. AppArmor enabled
    reason: KubeletReady
    status: &quot;True&quot;
    type: Ready
  daemonEndpoints:
    kubeletEndpoint:
      Port: 10250
  images:
  - names:
    - k8s.gcr.io/<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="f19a849394dc908198829483879483dc909c95c7c5b1829990c3c4c7">[email&#160;protected]</a>:956bea8c139620c9fc823fb81ff9b5647582b53bd33904302987d56ab24fc187
    - k8s.gcr.io/kube-apiserver-amd64:v1.11.3
    sizeBytes: 186676561
  nodeInfo:
    architecture: amd64
    bootID: 89ced22c-f7f8-4c4d-ad0d-d10887ab900e
    containerRuntimeVersion: docker://18.6.0
    kernelVersion: 4.4.0-62-generic
    kubeProxyVersion: v1.11.3
    kubeletVersion: v1.11.3
    machineID: 26ba042302eea8095d6576975c120eeb
    operatingSystem: linux
    osImage: Ubuntu 16.04.2 LTS
    systemUUID: 26ba042302eea8095d6576975c120eeb
</code></pre>
<p>可以看到 <code>kubelet</code> 不仅将自己注册给了 <code>kube-apiserver</code>，同时它所在机器的信息也都进行了上报，包括 CPU，内存，IP 信息等。</p>
<p>这其中有我们在第 2 节中提到的关于 <code>Node</code> 状态相关的一些信息，可以对照着看看。</p>
<p>当然这里除了这些信息外，还有些值得注意的，比如 <code>daemonEndpoints</code> 之类的，可以看到目前 <code>kubelet</code> 监听在了 <code>10250</code> 端口，这个端口可通过 <code>--port</code> 配置，但是之后会被废弃掉，我们是写入了 <code>/var/lib/kubelet/config.yaml</code> 的配置文件中。</p>
<pre><code>master $ cat /var/lib/kubelet/config.yaml
address: 0.0.0.0
apiVersion: kubelet.config.k8s.io/v1beta1
authentication:
  anonymous:
    enabled: false
  webhook:
    cacheTTL: 2m0s
    enabled: true
  x509:
    clientCAFile: /etc/kubernetes/pki/ca.crt
authorization:
  mode: Webhook
  webhook:
    cacheAuthorizedTTL: 5m0s
    cacheUnauthorizedTTL: 30s
cgroupDriver: cgroupfs
cgroupsPerQOS: true
clusterDNS:
- 10.96.0.10
clusterDomain: cluster.local
containerLogMaxFiles: 5
containerLogMaxSize: 10Mi
contentType: application/vnd.kubernetes.protobuf
cpuCFSQuota: true
cpuManagerPolicy: none
cpuManagerReconcilePeriod: 10s
enableControllerAttachDetach: true
enableDebuggingHandlers: true
enforceNodeAllocatable:
- pods
eventBurst: 10
eventRecordQPS: 5
evictionHard:
  imagefs.available: 15%
  memory.available: 100Mi
  nodefs.available: 10%
  nodefs.inodesFree: 5%
evictionPressureTransitionPeriod: 5m0s
failSwapOn: true
fileCheckFrequency: 20s
hairpinMode: promiscuous-bridge
healthzBindAddress: 127.0.0.1
healthzPort: 10248
httpCheckFrequency: 20s
imageGCHighThresholdPercent: 85
imageGCLowThresholdPercent: 80
imageMinimumGCAge: 2m0s
iptablesDropBit: 15
iptablesMasqueradeBit: 14
kind: KubeletConfiguration
kubeAPIBurst: 10
kubeAPIQPS: 5
makeIPTablesUtilChains: true
maxOpenFiles: 1000000
maxPods: 110
nodeStatusUpdateFrequency: 10s
oomScoreAdj: -999
podPidsLimit: -1
port: 10250
registryBurst: 10
registryPullQPS: 5
resolvConf: /etc/resolv.conf
rotateCertificates: true
runtimeRequestTimeout: 2m0s
serializeImagePulls: true
staticPodPath: /etc/kubernetes/manifests
streamingConnectionIdleTimeout: 4h0m0s
syncFrequency: 1m0s
volumeStatsAggPeriod: 1m0s
master $
</code></pre>
<p>这其中有一些需要关注的配置：</p>
<ul>
<li>
<p><code>maxPods</code>：最大的 <code>Pod</code> 数</p>
</li>
<li>
<p><code>healthzBindAddress</code> 和 <code>healthzPort</code>：配置了健康检查所监听的地址和端口</p>
<p>我们可用以下方式进行验证：</p>
<pre><code>master $ curl 127.0.0.1:10248/healthz
ok 
</code></pre>
</li>
<li>
<p><code>authentication</code> 和 <code>authorization</code> ：认证授权相关</p>
</li>
<li>
<p><code>evictionHard</code>：涉及到 <code>kubelet</code> 的驱逐策略，对 <code>Pod</code> 调度分配之类的影响很大</p>
</li>
</ul>
<p>其余部分，可参考<a href="https://kubernetes.io/docs/tasks/administer-cluster/out-of-resource/">手册内容</a></p>
<h3>Pod 管理</h3>
<p>从上面的配置以及我们之前的介绍中，<code>kube-scheduler</code> 处理了 <code>Pod</code> 应该调度至哪个 <code>Node</code>，而 <code>kubelet</code> 则是保障该 <code>Pod</code> 能按照预期，在对应 <code>Node</code> 上启动并保持工作。</p>
<p>同时，<code>kubelet</code> 在保障 <code>Pod</code> 能按预期工作，主要是做了两方面的事情：</p>
<ul>
<li>健康检查：通过 <code>LivenessProbe</code> 和 <code>ReadinessProbe</code> 探针进行检查，判断是否健康及是否已经准备好接受请求。</li>
<li>资源监控：通过 <code>cAdvisor</code> 进行资源监。</li>
</ul>
<h2><code>kubelet</code> 是如何工作的</h2>
<p>大致的功能已经介绍了，我们来看下它大体的实现。</p>
<p>首先是在 <code>cmd/kubelet/app/server.go</code> 文件中的 <code>Run</code> 方法：</p>
<pre><code>func Run(s *options.KubeletServer, kubeDeps *kubelet.Dependencies, stopCh &lt;-chan struct{}) error {
	glog.Infof(&quot;Version: %+v&quot;, version.Get())
	if err := initForOS(s.KubeletFlags.WindowsService); err != nil {
		return fmt.Errorf(&quot;failed OS init: %v&quot;, err)
	}
	if err := run(s, kubeDeps, stopCh); err != nil {
		return fmt.Errorf(&quot;failed to run Kubelet: %v&quot;, err)
	}
	return nil
}
</code></pre>
<p>这个方法看起来很简单那，它是在读取完一系列的配置和校验之后开始被调用的，在调用过程中，会在日志中输出当前的版本号，如果你的 <code>kubelet</code> 已经正常运行，当你执行 <code>journalctl -u kubelet</code> 的时候，便会看到一条相关的日志输出。</p>
<p>之后，便是一个 <code>run</code> 方法，其中包含着各种环境检查，容器管理，<code>cAdvisor</code> 初始化之类的操作，直到 <code>kubelet</code> 基本正确运行后，则会调用 <code>pkg/kubelet/kubelet.go</code> 中的一个 <code>BirthCry</code> 方法，该方法从命名就可以看出来，它其实就是宣告 <code>kubelet</code> 已经启动：</p>
<pre><code>func (kl *Kubelet) BirthCry() {
	kl.recorder.Eventf(kl.nodeRef, v1.EventTypeNormal, events.StartingKubelet, &quot;Starting kubelet.&quot;)
}
</code></pre>
<p>后续则是关于注册，<code>Pod</code> 管理以及资源相关的处理逻辑，内容较多，这里就不再展开了。</p>
<h2>总结</h2>
<p>本节中我们介绍了 <code>kubelet</code> 的主要功能和基本实现，了解到了它不仅可将自身注册到集群，同时还承担着保障 <code>Pod</code> 可在该 <code>Node</code> 上按预期工作。另外 <code>kubelet</code> 其实还承担着清理 <code>Node</code> 上一些由 K8S 调度 <code>Pod</code> 所造成的磁盘占用之类的工作。</p>
<p>从上面的配置中基本能看出来一些，这部分的功能大多数情况下不需要大家人为干预，所以也就不再展开了。</p>
<p>当 <code>Pod</code> 在 <code>Node</code> 上正常运行之后，若是需要对外提供服务，则需要将其暴露出来。下节，我们来介绍下 <code>kube-proxy</code> 是如何来处理这些工作的。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;庖丁解牛：kube-scheduler.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;庖丁解牛：kube-proxy.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346126a6b70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
