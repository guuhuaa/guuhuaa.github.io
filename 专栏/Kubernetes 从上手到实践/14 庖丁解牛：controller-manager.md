<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>14 庖丁解牛：controller-manager.md</title>
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

                    <a class="current-tab" href="14&#32;庖丁解牛：controller-manager.md">14 庖丁解牛：controller-manager.md</a>
                    

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
                        <div><h1>14 庖丁解牛：controller-manager</h1>
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
<p>在第 3 节《宏观认识：整体架构》 中，我们也认识到了 <code>Controller Manager</code> 的存在，知道了 Master 是 K8S 是集群的大脑，而它则是 Master 中最繁忙的部分。为什么这么说？本节我们一同来看看它为何如此繁忙。</p>
<p><strong>注意：Controller Manager 实际由 kube-controller-manager 和 cloud-controller-manager 两部分组成，cloud-controller-manager 则是为各家云厂商提供了一个抽象的封装，便于让各厂商使用各自的 provide。本文只讨论 kube-controller-manager，为了避免混淆，下文统一使用 kube-controller-manager。</strong></p>
<h2><code>kube-controller-manager</code> 是什么</h2>
<p>一句话来讲 <code>kube-controller-manager</code> 是一个嵌入了 K8S 核心控制循环的守护进程。</p>
<p>这里的重点是</p>
<ul>
<li>嵌入：它已经内置了相关逻辑，可独立进行部署。我们在第 5 节下载 K8S 服务端二进制文件解压后，便可以看到 <code>kube-controller-manager</code> 的可执行文件，不过我们使用的是 <code>kubeadm</code> 进行的部署，它会默认使用 <code>k8s.gcr.io/kube-controller-manager</code> 的镜像。我们直接来看下实际情况：</li>
</ul>
<pre><code>master $ kubectl -n kube-system describe pods -l component=kube-controller-manager
Name:               kube-controller-manager-master
Namespace:          kube-system
Priority:           2000000000
PriorityClassName:  system-cluster-critical
Node:               master/172.17.0.35
Start Time:         Mon, 10 Dec 2018 07:14:21 +0000
Labels:             component=kube-controller-manager
                    tier=control-plane
Annotations:        kubernetes.io/config.hash=c7ed7a8fa5c430410e84970f8ee7e067
                    kubernetes.io/config.mirror=c7ed7a8fa5c430410e84970f8ee7e067
                    kubernetes.io/config.seen=2018-12-10T07:14:21.685626322Z
                    kubernetes.io/config.source=file
                    scheduler.alpha.kubernetes.io/critical-pod=
Status:             Running
IP:                 172.17.0.35
Containers:
  kube-controller-manager:
    Container ID:  docker://0653e71ae4287608726490b724c3d064d5f1556dd89b7d3c618e97f0e7f2a533
    Image:         k8s.gcr.io/kube-controller-manager-amd64:v1.11.3
    Image ID:      docker-pullable://k8s.gcr.io/<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="f59e809790d8969a9b81879a99999087d898949b94929087d8949891c3c1b5869d94c7c0c3">[email&#160;protected]</a>:a6d115bb1c0116036ac6e6e4d504665bc48879c421a450566c38b3b726f0a123
    Port:          &lt;none&gt;
    Host Port:     &lt;none&gt;
    Command:
      kube-controller-manager
      --address=127.0.0.1
      --cluster-signing-cert-file=/etc/kubernetes/pki/ca.crt
      --cluster-signing-key-file=/etc/kubernetes/pki/ca.key
      --controllers=*,bootstrapsigner,tokencleaner
      --kubeconfig=/etc/kubernetes/controller-manager.conf
      --leader-elect=true
      --root-ca-file=/etc/kubernetes/pki/ca.crt
      --service-account-private-key-file=/etc/kubernetes/pki/sa.key
      --use-service-account-credentials=true
    State:          Running
      Started:      Mon, 10 Dec 2018 07:14:24 +0000
    Ready:          True
    Restart Count:  0
    Requests:
      cpu:        200m
    Liveness:     http-get http://127.0.0.1:10252/healthz delay=15s timeout=15s period=10s #success=1 #failure=8
    Environment:  &lt;none&gt;
    Mounts:
      /etc/ca-certificates from etc-ca-certificates (ro)
      /etc/kubernetes/controller-manager.conf from kubeconfig (ro)
      /etc/kubernetes/pki from k8s-certs (ro)
      /etc/ssl/certs from ca-certs (ro)
      /usr/libexec/kubernetes/kubelet-plugins/volume/exec from flexvolume-dir (rw)
      /usr/local/share/ca-certificates from usr-local-share-ca-certificates (ro)
      /usr/share/ca-certificates from usr-share-ca-certificates (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  usr-share-ca-certificates:
    Type:          HostPath (bare host directory volume)
    Path:          /usr/share/ca-certificates
    HostPathType:  DirectoryOrCreate
  usr-local-share-ca-certificates:
    Type:          HostPath (bare host directory volume)
    Path:          /usr/local/share/ca-certificates
    HostPathType:  DirectoryOrCreate
  etc-ca-certificates:
    Type:          HostPath (bare host directory volume)
    Path:          /etc/ca-certificates
    HostPathType:  DirectoryOrCreate
  k8s-certs:
    Type:          HostPath (bare host directory volume)
    Path:          /etc/kubernetes/pki
    HostPathType:  DirectoryOrCreate
  ca-certs:
    Type:          HostPath (bare host directory volume)
    Path:          /etc/ssl/certs
    HostPathType:  DirectoryOrCreate
  kubeconfig:
    Type:          HostPath (bare host directory volume)
    Path:          /etc/kubernetes/controller-manager.conf
    HostPathType:  FileOrCreate
  flexvolume-dir:
    Type:          HostPath (bare host directory volume)
    Path:          /usr/libexec/kubernetes/kubelet-plugins/volume/exec
    HostPathType:  DirectoryOrCreate
QoS Class:         Burstable
Node-Selectors:    &lt;none&gt;
Tolerations:       :NoExecute
Events:            &lt;none&gt;
master
</code></pre>
<p>这是使用 <code>kubeadm</code> 搭建的集群中的 <code>kube-controller-manager</code> 的 <code>Pod</code>，首先可以看到它所使用的镜像，其次可以看到它使用的一系列参数，最后它在 <code>10252</code> 端口提供了健康检查的接口。稍后我们再展开。</p>
<ul>
<li>控制循环：这里拆解为两部分： <strong>控制</strong> 和 <strong>循环</strong> ，它所控制的是集群的状态；至于循环它当然是会有个循环间隔的，这里有个参数可以进行控制。</li>
<li>守护进程：这个就不单独展开了。</li>
</ul>
<h2><code>kube-controller-manager</code> 有什么作用</h2>
<p>前面已经说了它一个很关键的点 “控制”：它通过 <code>kube-apiserver</code> 提供的信息持续的监控集群状态，并尝试将集群调整至预期的状态。由于访问 <code>kube-apiserver</code> 也需要通过认证，授权等过程，所以可以看到上面启动 <code>kube-controller-manager</code> 时提供了一系列的参数。</p>
<p>比如，当我们创建了一个 <code>Deployment</code>，默认副本数为 1 ，当我们把 <code>Pod</code> 删除后，<code>kube-controller-manager</code> 会按照原先的预期，重新创建一个 <code>Pod</code> 。下面举个例子：</p>
<pre><code>master $ kubectl run redis --image='redis'
deployment.apps/redis created
master $ kubectl get all
NAME                        READY     STATUS    RESTARTS   AGE
pod/redis-bb7894d65-w2rsp   1/1       Running   0          3m

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    &lt;none&gt;        443/TCP   18m

NAME                    DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/redis   1         1         1            1           3m

NAME                              DESIRED   CURRENT   READY     AGE
replicaset.apps/redis-bb7894d65   1         1         1         3m
master $ kubectl delete pod/redis-bb7894d65-w2rsp
pod &quot;redis-bb7894d65-w2rsp&quot; deleted
master $ kubectl get all  # 可以看到已经重新运行了一个 Pod
NAME                        READY     STATUS    RESTARTS   AGE
pod/redis-bb7894d65-62ftk   1/1       Running   0          16s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    &lt;none&gt;        443/TCP   19m

NAME                    DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/redis   1         1         1            1           4m

NAME                              DESIRED   CURRENT   READY     AGE
replicaset.apps/redis-bb7894d65   1         1         1         4m
</code></pre>
<p>我们来看下 <code>kube-controller-manager</code> 的日志：</p>
<pre><code>master $ kubectl -n kube-system logs -l component=kube-controller-manager --tail=5
I1210 09:30:17.125377       1 node_lifecycle_controller.go:945] Controller detected that all Nodes are not-Ready. Entering master disruption mode.
I1210 09:31:07.140539       1 node_lifecycle_controller.go:972] Controller detected that some Nodes are Ready. Exiting master disruption mode.
I1210 09:43:30.377649       1 event.go:221] Event(v1.ObjectReference{Kind:&quot;Deployment&quot;, Namespace:&quot;default&quot;, Name:&quot;redis&quot;, UID:&quot;0d1cb2d7-fc60-11e8-a361-0242ac110074&quot;, APIVersion:&quot;apps/v1&quot;, ResourceVersion:&quot;1494&quot;, FieldPath:&quot;&quot;}): type: 'Normal' reason: 'ScalingReplicaSet' Scaled up replica setredis-bb7894d65 to 1
I1210 09:43:30.835149       1 event.go:221] Event(v1.ObjectReference{Kind:&quot;ReplicaSet&quot;, Namespace:&quot;default&quot;, Name:&quot;redis-bb7894d65&quot;, UID:&quot;0d344d15-fc60-11e8-a361-0242ac110074&quot;, APIVersion:&quot;apps/v1&quot;, ResourceVersion:&quot;1495&quot;, FieldPath:&quot;&quot;}): type: 'Normal' reason: 'SuccessfulCreate' Created pod:redis-bb7894d65-w2rsp
I1210 09:47:41.658781       1 event.go:221] Event(v1.ObjectReference{Kind:&quot;ReplicaSet&quot;, Namespace:&quot;default&quot;, Name:&quot;redis-bb7894d65&quot;, UID:&quot;0d344d15-fc60-11e8-a361-0242ac110074&quot;, APIVersion:&quot;apps/v1&quot;, ResourceVersion:&quot;1558&quot;, FieldPath:&quot;&quot;}): type: 'Normal' reason: 'SuccessfulCreate' Created pod:redis-bb7894d65-62ftk
</code></pre>
<p>可以看到它先观察到有 <code>Deployment</code> 的事件，然后 <code>ScalingReplicaSet</code> 进而创建了对应的 <code>Pod</code>。 而当我们删掉正在运行的 <code>Pod</code> 后，它便会重新创建 <code>Pod</code> 使集群状态符合原先的预期状态。</p>
<p>同时，注意 <code>Pod</code> 的名字已经发生了变化。</p>
<h2><code>kube-controller-manager</code> 是如何工作的</h2>
<p>在 <code>cmd/kube-controller-manager/app/controllermanager.go</code> 中列出了大多数的 <code>controllermanager</code>，他们对 <code>controllermanager</code> 函数的实际调用都在 <code>cmd/kube-controller-manager/app/core.go</code> 中，我们以 <code>PodGC</code> 为例：</p>
<pre><code>func startPodGCController(ctx ControllerContext) (bool, error) {
	go podgc.NewPodGC(
		ctx.ClientBuilder.ClientOrDie(&quot;pod-garbage-collector&quot;),
		ctx.InformerFactory.Core().V1().Pods(),
		int(ctx.ComponentConfig.PodGCController.TerminatedPodGCThreshold),
	).Run(ctx.Stop)
	return true, nil
}
</code></pre>
<p>在前两节中我们已经对 <code>kube-apiserver</code> 和 <code>etcd</code> 有了一些基本的认识，这里它主要会去 watch 相关的资源，但是出于性能上的考虑，也不能过于频繁的去请求 <code>kube-apiserver</code> 或者永久 watch ，所以在实现上借助了 <a href="https://github.com/kubernetes/client-go">client-go</a> 的 <code>informer</code> 包，相当于是实现了一个本地的二级缓存。这里不做过多展开。</p>
<p>它最终会调用 <code>PodGC</code> 的具体实现，位置在 <code>pkg/controller/podgc/gc_controller.go</code> 中：</p>
<pre><code>func NewPodGC(kubeClient clientset.Interface, podInformer coreinformers.PodInformer, terminatedPodThreshold int) *PodGCController {
	if kubeClient != nil &amp;&amp; kubeClient.CoreV1().RESTClient().GetRateLimiter() != nil {
		metrics.RegisterMetricAndTrackRateLimiterUsage(&quot;gc_controller&quot;, kubeClient.CoreV1().RESTClient().GetRateLimiter())
	}
	gcc := &amp;PodGCController{
		kubeClient:             kubeClient,
		terminatedPodThreshold: terminatedPodThreshold,
		deletePod: func(namespace, name string) error {
			glog.Infof(&quot;PodGC is force deleting Pod: %v:%v&quot;, namespace, name)
			return kubeClient.CoreV1().Pods(namespace).Delete(name, metav1.NewDeleteOptions(0))
		},
	}

	gcc.podLister = podInformer.Lister()
	gcc.podListerSynced = podInformer.Informer().HasSynced

	return gcc
}
</code></pre>
<p>代码也比较直观，不过这里可以看到有一个注册 <code>metrics</code> 的过程，实际上 <code>kube-controller-manager</code> 在前面的 <code>10252</code> 端口上不仅暴露出来了一个 <code>/healthz</code> 接口，还暴露出了一个 <code>/metrics</code> 的接口，可用于进行监控之类的。</p>
<pre><code>master $ kubectl -n kube-system get pod -l component=kube-controller-manager
NAME                             READY     STATUS    RESTARTS   AGE
kube-controller-manager-master   1/1       Running   1          2m
master $ kubectl -n kube-system exec -it kube-controller-manager-master sh
/ # wget -qO- http://127.0.0.1:10252/metrics|grep gc_controller
# HELP gc_controller_rate_limiter_use A metric measuring the saturation of the rate limiter for gc_controller
# TYPE gc_controller_rate_limiter_use gauge
gc_controller_rate_limiter_use 0
</code></pre>
<h2>总结</h2>
<p>在本节中，我们介绍了 <code>kube-controller-manager</code> 以及它在 K8S 中主要是将集群调节至预期的状态，并提供出了 <code>/metrics</code> 的接口可供监控。</p>
<p><code>kube-controller-manager</code> 中有很多的 controller 大多数是默认开启的，当然也有默认关闭的，比如 <code>bootstrapsigner</code> 和 <code>tokencleaner</code>，在我们启动 <code>kube-controller-manager</code> 的时候，可通过 <code>--controllers</code> 的参数进行控制，就比如上面例子中 <code>--controllers=*,bootstrapsigner,tokencleaner</code> 表示开启所有默认开启的以及 <code>bootstrapsigner</code> 和 <code>tokencleaner</code> 。</p>
<p>下节，我们将学习另一个与资源调度有关的组件 <code>kube-scheduler</code>，了解下它对我们使用集群所带来的意义。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="13&#32;庖丁解牛：etcd.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="15&#32;庖丁解牛：kube-scheduler.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346091c7f70ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
