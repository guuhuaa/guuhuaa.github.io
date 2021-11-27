<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>19 使用 Rook 构建生产可用存储环境实践.md</title>
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

                    
                    <a href="00&#32;为什么我们要学习&#32;Kubernetes&#32;技术.md">00 为什么我们要学习 Kubernetes 技术.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;重新认识&#32;Kubernetes&#32;的核心组件.md">01 重新认识 Kubernetes 的核心组件.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;深入理解&#32;Kubernets&#32;的编排对象.md">02 深入理解 Kubernets 的编排对象.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;DevOps&#32;场景下落地&#32;K8s&#32;的困难分析.md">03 DevOps 场景下落地 K8s 的困难分析.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;微服务应用场景下落地&#32;K8s&#32;的困难分析.md">04 微服务应用场景下落地 K8s 的困难分析.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;解决&#32;K8s&#32;落地难题的方法论提炼.md">05 解决 K8s 落地难题的方法论提炼.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;练习篇：K8s&#32;核心实践知识掌握.md">06 练习篇：K8s 核心实践知识掌握.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;容器引擎&#32;containerd&#32;落地实践.md">07 容器引擎 containerd 落地实践.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;K8s&#32;集群安装工具&#32;kubeadm&#32;的落地实践.md">08 K8s 集群安装工具 kubeadm 的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;南北向流量组件&#32;IPVS&#32;的落地实践.md">09 南北向流量组件 IPVS 的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;东西向流量组件&#32;Calico&#32;的落地实践.md">10 东西向流量组件 Calico 的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;服务发现&#32;DNS&#32;的落地实践.md">11 服务发现 DNS 的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;练习篇：K8s&#32;集群配置测验.md">12 练习篇：K8s 集群配置测验.md</a>

                </li>
                <li>

                    
                    <a href="13&#32;理解对方暴露服务的对象&#32;Ingress&#32;和&#32;Service.md">13 理解对方暴露服务的对象 Ingress 和 Service.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;应用网关&#32;OpenResty&#32;对接&#32;K8s&#32;实践.md">14 应用网关 OpenResty 对接 K8s 实践.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;Service&#32;层引流技术实践.md">15 Service 层引流技术实践.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;Cilium&#32;容器网络的落地实践.md">16 Cilium 容器网络的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;应用流量的优雅无损切换实践.md">17 应用流量的优雅无损切换实践.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;练习篇：应用流量无损切换技术测验.md">18 练习篇：应用流量无损切换技术测验.md</a>

                </li>
                <li>

                    <a class="current-tab" href="19&#32;使用&#32;Rook&#32;构建生产可用存储环境实践.md">19 使用 Rook 构建生产可用存储环境实践.md</a>
                    

                </li>
                <li>

                    
                    <a href="20&#32;有状态应用的默认特性落地分析.md">20 有状态应用的默认特性落地分析.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;案例：分布式&#32;MySQL&#32;集群工具&#32;Vitess&#32;实践分析.md">21 案例：分布式 MySQL 集群工具 Vitess 实践分析.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;存储对象&#32;PV、PVC、Storage&#32;Classes&#32;的管理落地实践.md">22 存储对象 PV、PVC、Storage Classes 的管理落地实践.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;K8s&#32;集群中存储对象灾备的落地实践.md">23 K8s 集群中存储对象灾备的落地实践.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;练习篇：K8s&#32;集群配置测验.md">24 练习篇：K8s 集群配置测验.md</a>

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
                        <div><h1>19 使用 Rook 构建生产可用存储环境实践</h1>
<p>Rook 是基于 Kubernetes 之上构建的存储服务框架。它支持 Ceph、NFS 等多种底层存储的创建和管理。帮助系统管理员自动化维护存储的整个生命周期。存储的整个生命周期包括部署、启动、配置、申请、扩展、升级、迁移、灾难恢复、监控和资源管理等，看着就让笔者觉得事情不少，Rook 的目标就是降低运维的难度，让 Kubernetes 和 Rook 来帮你托管解决这些任务。</p>
<h3>Rook 管理 Ceph 集群</h3>
<p>Ceph 分布式存储是 Rook 支持的第一个标记为 Stable 的编排存储引擎，在笔者验证 Rook 操作 Ceph 的过程中发现，其社区文档、脚本都放在一起，初次新手很难知道如何一步一步体验 Rook 搭建 Ceph 的过程。这从一个侧面反应了分布式存储的技术难度和兼容性是一个长期的迭代过程，Rook 的本意是为了降低部署管理 Ceph 集群的难度，但是事与愿违，初期使用的过程并不友好，有很多不知名的问题存在官方文档中。</p>
<p><img src="assets/45821220-16c6-11eb-8b57-67f291f7f7f6.jpg" alt="16-1-rook-arch.png" /></p>
<p>在安装 Ceph 前要注意，目前最新的 Ceph 支持的存储后端 BlueStore 仅支持裸设备，不支持在本地文件系统之上建立存储块。因为 Rook 文档的混乱，一开始我们需要自己找到安装脚本目录，它在</p>
<blockquote>
<p><a href="https://github.com/rook/rook/tree/master/cluster/examples/kubernetes/ceph">https://github.com/rook/rook/tree/master/cluster/examples/kubernetes/ceph</a></p>
</blockquote>
<pre><code class="language-bash">$ git clone https://github.com/rook/rook.git
$ cd rook
$ git checkout release-1.4
$ cd cluster/examples/kubernetes/ceph

$ kubectl create -f common.yaml
# 检查 namesapce 是否有 rook-ceph 了
$ kubectl get namespace
$ kubectl create -f operator.yaml
# 上述的步骤必须确定 pods 已经处于 running or complete 才能做下一个阶段，否则很有可能会 fail，上述的步骤需要等一会。
$ kubectl create -f cluster.yaml
# 等待 Ceph 集群创建成功。

$ kubectl -n rook-ceph get pods
# mgr 1, mon 3, 
# rook-ceph-crashcollector (有几个 node 就有几个)
# rook-ceph-osd (有几个 disk，就会有几个 pod，排序从 0 开始)

</code></pre>
<p>Ceph 的问题很多，经常需要使用工具箱查看一些情况，按照如下步骤部署：</p>
<pre><code class="language-bash">$ kubectl create -f toolbox.yaml
$ kubectl -n rook-ceph get pods | grep ceph-tools
rook-ceph-tools-649c4dd574-gw8tx   1/1  Running  0   3m20s
$ kubectl -n rook-ceph exec -it rook-ceph-tools-649c4dd574-gw8tx bash
$ ceph -s
cluster:
    id:     9ca03dd5-05bc-467f-89a8-d3dfce3b9430
    health: HEALTH_OK

  services:
    mon: 3 daemons, quorum a,d,e (age 12m)
    mgr: a(active, since 8m)
    osd: 44 osds: 44 up (since 13m), 44 in (since 13m)

  data:
    pools:   1 pools, 1 pgs
    objects: 0 objects, 0 B
    usage:   45 GiB used, 19 TiB / 19 TiB avail
    pgs:     1 active+clean
# ceph 集群可以使用的容量
$ ceph df
# ceph osd 与 node 的关系分布
$ ceph osd tree
# 删除 ceph toolbox 工具
$ kubectl delete -f toolbox.yaml

</code></pre>
<p>使用 Dashboard 查看 Ceph 运行情况：</p>
<pre><code class="language-bash">$ vim dashboard-external-https.yaml
apiVersion: v1
kind: Service
metadata:
  name: rook-ceph-mgr-dashboard-external-https
  namespace: rook-ceph
  labels:
    app: rook-ceph-mgr
    rook_cluster: rook-ceph
spec:
  ports:
  - name: dashboard
    port: 8443
    protocol: TCP
    targetPort: 8443
  selector:
    app: rook-ceph-mgr
    rook_cluster: rook-ceph
  sessionAffinity: None
  type: NodePort
$ kubectl create -f dashboard-external-https.yaml
$ kubectl -n rook-ceph get service
rook-ceph-mgr-dashboard-external-https   NodePort    10.107.117.151   &lt;none&gt;        8443:31955/TCP      8m23s

</code></pre>
<p>访问地址是 31955，https://master_ip:31955 就可以访问。账号是 admin，密码可以在线查到：</p>
<pre><code class="language-bsah">$ kubectl -n rook-ceph get secret rook-ceph-dashboard-password -o jsonpath=&quot;{['data']['password']}&quot; | base64 --decode &amp;&amp; echo

</code></pre>
<p>清空 Ceph：</p>
<pre><code>$ cd /rook/cluster/examples/kubernetes/ceph
$ kubectl -n rook-ceph delete cephcluster rook-ceph
$ kubectl -n rook-ceph get cephcluster
# 确认 rook-ceph 被删除
$ kubectl delete -f operator.yaml
# 删除集群
$ kubectl delete -f common.yaml
$ kubectl delete -f cluster.yaml

</code></pre>
<h3>用 Rook 管理 NFS 文件系统</h3>
<p>NFS 文件系统目前在国内企业还是很常见的一种存储方案。用 Rook 来管理 NFS 文件系统可以极大的方便开发者的存储环境。安装 rook 之前需要先安装 NFS Client 安装包。在 CentOS 节点上安装 nf-utils，在 Ubuntu 节点上安装 nf-common。然后就可以安装 Rook 了。步骤如下：</p>
<pre><code class="language-bash">git clone --single-branch --branch v1.4.6 https://github.com/rook/rook.git
cd rook/cluster/examples/kubernetes/nfs
kubectl create -f common.yaml
kubectl create -f provisioner.yaml
kubectl create -f operator.yaml

#查看运行情况
[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="98eaf7f7ecd8fcfdeeb5f5f6ffb5ecfdf5e8">[email&#160;protected]</a> ~]# kubectl -n rook-nfs-system get pod
NAME                                   READY   STATUS    RESTARTS   AGE
rook-nfs-operator-59fb455d77-2cxn4     1/1     Running   0          75m
rook-nfs-provisioner-b4bbf4cc4-qrzqd   1/1     Running   1          75m

</code></pre>
<p>创建权限，rbac.yaml 内容如下：</p>
<pre><code class="language-yaml">---
apiVersion: v1
kind: Namespace
metadata:
  name:  rook-nfs
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: rook-nfs-server
  namespace: rook-nfs
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: rook-nfs-provisioner-runner
rules:
  - apiGroups: [&quot;&quot;]
    resources: [&quot;persistentvolumes&quot;]
    verbs: [&quot;get&quot;, &quot;list&quot;, &quot;watch&quot;, &quot;create&quot;, &quot;delete&quot;]
  - apiGroups: [&quot;&quot;]
    resources: [&quot;persistentvolumeclaims&quot;]
    verbs: [&quot;get&quot;, &quot;list&quot;, &quot;watch&quot;, &quot;update&quot;]
  - apiGroups: [&quot;storage.k8s.io&quot;]
    resources: [&quot;storageclasses&quot;]
    verbs: [&quot;get&quot;, &quot;list&quot;, &quot;watch&quot;]
  - apiGroups: [&quot;&quot;]
    resources: [&quot;events&quot;]
    verbs: [&quot;create&quot;, &quot;update&quot;, &quot;patch&quot;]
  - apiGroups: [&quot;&quot;]
    resources: [&quot;services&quot;, &quot;endpoints&quot;]
    verbs: [&quot;get&quot;]
  - apiGroups: [&quot;policy&quot;]
    resources: [&quot;podsecuritypolicies&quot;]
    resourceNames: [&quot;rook-nfs-policy&quot;]
    verbs: [&quot;use&quot;]
  - apiGroups: [&quot;&quot;]
    resources: [&quot;endpoints&quot;]
    verbs: [&quot;get&quot;, &quot;list&quot;, &quot;watch&quot;, &quot;create&quot;, &quot;update&quot;, &quot;patch&quot;]
  - apiGroups:
    - nfs.rook.io
    resources:
    - &quot;*&quot;
    verbs:
    - &quot;*&quot;
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: rook-nfs-provisioner-runner
subjects:
  - kind: ServiceAccount
    name: rook-nfs-server
     # replace with namespace where provisioner is deployed
    namespace: rook-nfs
roleRef:
  kind: ClusterRole
  name: rook-nfs-provisioner-runner
  apiGroup: rbac.authorization.k8s.io

</code></pre>
<p>执行 yaml 创建权限：</p>
<pre><code class="language-bash">kubectl create -f rbac.yaml

</code></pre>
<p>当前主流的做法是采用动态申请资源的方式创建 NFSServer，步骤如下：</p>
<pre><code class="language-bash">kubectl create -f nfs.yaml

# sc.yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  labels:
    app: rook-nfs
  name: rook-nfs-share1
parameters:
  exportName: share1
  nfsServerName: rook-nfs
  nfsServerNamespace: rook-nfs
provisioner: rook.io/nfs-provisioner
reclaimPolicy: Delete
volumeBindingMode: Immediate

</code></pre>
<p><code>kubectl create -f sc.yaml</code> 将创建 StorageClass，然后就可以申请资源：</p>
<pre><code class="language-yaml">apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: rook-nfs-pv-claim
spec:
  storageClassName: &quot;rook-nfs-share1&quot;
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 1Mi

</code></pre>
<p><code>kubectl create -f pvc.yaml</code> 将创建一份文件卷。校验结果：</p>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="34465b5b407450514219595a531940515944">[email&#160;protected]</a> nfs]# kubectl get pvc
NAME                STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS      AGE
rook-nfs-pv-claim   Bound    pvc-504eb26d-1b6f-4ad8-9318-75e637ab50c7   1Mi        RWX            rook-nfs-share1   7m5s

</code></pre>
<p>测试使用的案例：</p>
<pre><code class="language-bash">&gt; kubectl create -f busybox-rc.yaml
&gt; kubectl create -f web-rc.yaml

&gt; kubectl get pod -l app=nfs-demo

&gt; kubectl create -f web-service.yaml

&gt; echo; kubectl exec $(kubectl get pod -l app=nfs-demo,role=busybox -o jsonpath='{.items[0].metadata.name}') -- wget -qO- http://$(kubectl get services nfs-web -o jsonpath='{.spec.clusterIP}'); echo

Thu Oct 22 19:28:55 UTC 2015
nfs-busybox-w3s4t

</code></pre>
<p>当你发现 NFS Server 没有运行起来，可以用这一行命令查看问题：</p>
<pre><code class="language-bash">kubectl -n rook-nfs-system logs -l app=rook-nfs-operator

</code></pre>
<h3>总结</h3>
<p>Rook 项目从笔者入手来，其目标定位还是很准，并且真实的解决了简化 Ceph 安装配置的痛点，并且依据 Ceph 使用的经验开始注入更多的存储驱动，如 NFS 存储驱动。使用起来并不复杂，但是它的文档实在是太糟糕了。社区中也没有人来专门维护这套文档，导致文章中很多描述都是过期的，你根本不清楚如何配置。一不小心就会配置错误。所以大家在使用过程中，还是要仔细熟悉一遍 yaml 文档的内容，了解到它的功能后在安装，就会事半功倍。这种不完善其实对开源技术爱好者来说，也是一种机会，让你通过修改文档的方式参与到 Rook 这个项目中。以我梳理一遍之后，通过最新版本的安装步骤，你可以几分钟就可以部署自己的分布式存储环境，Rook 确实事半功倍，值得推荐并大量实践使用。</p>
<h3>参考资料</h3>
<ul>
<li><a href="https://draveness.me/papers-ceph/">https://draveness.me/papers-ceph/</a></li>
<li><a href="https://rook.io/docs/rook/v1.4/nfs.html">https://rook.io/docs/rook/v1.4/nfs.html</a></li>
</ul>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="18&#32;练习篇：应用流量无损切换技术测验.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="20&#32;有状态应用的默认特性落地分析.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346a6bc3570ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Kubernetes%20%E5%AE%9E%E8%B7%B5%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
