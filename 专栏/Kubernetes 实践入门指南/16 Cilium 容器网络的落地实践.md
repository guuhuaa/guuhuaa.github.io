<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16 Cilium 容器网络的落地实践.md</title>
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

                    <a class="current-tab" href="16&#32;Cilium&#32;容器网络的落地实践.md">16 Cilium 容器网络的落地实践.md</a>
                    

                </li>
                <li>

                    
                    <a href="17&#32;应用流量的优雅无损切换实践.md">17 应用流量的优雅无损切换实践.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;练习篇：应用流量无损切换技术测验.md">18 练习篇：应用流量无损切换技术测验.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;使用&#32;Rook&#32;构建生产可用存储环境实践.md">19 使用 Rook 构建生产可用存储环境实践.md</a>

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
                        <div><h1>16 Cilium 容器网络的落地实践</h1>
<p>随着越来越多的企业采用 Kubernetes，围绕多云、安全、可见性和可扩展性等新要求，可编程数据平面的需求用例范围越来越广。此外，服务网格和无服务器等新技术对 Kubernetes 底层提出了更多的定制化要求。这些新需求都有一些共同点：它们需要一个更可编程的数据平面，能够在不牺牲性能的情况下执行 Kubernetes 感知的网络数据操作。</p>
<p>Cilium 项目通过引入扩展的伯克利数据包过滤器（eBPF）技术，在 Linux 内核内向网络栈暴露了可编程的钩子。使得网格数据包不需要在用户和内核空间之间来回切换就可以通过上下文快速进行数据交换操作。这是一种新型的网络范式，它也是 Cilium 容器网络项目的核心思想。</p>
<p><img src="assets/e071dc20-0c99-11eb-8b8d-fb5aa176e4a4.jpg" alt="14-1-cilium-cni" /></p>
<h3>为什么需要落地 Cilium 容器网络？</h3>
<p>Kubernetes 的容器网络方案发展至今，一直是百家争鸣，各有特色。之前因为 CNI 网络方案不成熟，大家用起来都是战战兢兢，时刻提防容器网络给业务带来不可接受的效果，随即就把容器网络替换成主机网络。随着时间的磨砺，当前主流的容器网络方案如 Calico 等已经经历成百上千次生产环境的应用考验，大部分场景下都可以达到用户可以接受的网络性能指标。因为成功经验开始增多，用户也开始大规模启用容器网络的上线了。随着业务流量的引入越来越大，用户对 Kubernetes 网络的认知也趋于一致。大致分为两大类，一类是 Cluster IP，是一层反向代理的虚拟网络；一类是 Pod IP，是容器间交互数据的网络数据平面。对于反向代理虚拟网络的技术实现，早期 kube-proxy 是采用 iptables，后来引入 IPVS 也解决了大规模容器集群的网络编排的性能问题。这样的实现结构你从顶端俯瞰会明显感知到 Kubernetes 网络数据平台非常零散，并没有实现一套体系的网络策略编排和隔离。显然，这样的技术结构也无法引入数据可视化能力。这也是 Istio 服务网格引入后，通过增加 envoy sidecar 来实现网络流量可视化带来了机会。但是这种附加的边界网关毕竟又对流量增加了一层反向代理，让网络性能更慢了。Cilium 原生通过 eBPF 编排网络数据，让可视化更简单。</p>
<p>Cilium 还有一个强项就是通过 eBPF 是可以自定义隔离策略的，这样就可以在非信任的主机环境编排更多的容器网络隔离成多租户环境，让用户不在担心数据的泄露，可以更专注在数据业务的连通性上。因为 eBPF 的可编程性，我们还能依据业务需求，增加各种定制化插件，让数据平台可以更加灵活安全。</p>
<h3>Cilium CNI 实现</h3>
<p>Cilium Agent、Cilium CLI Client 和 CNI Plugin 运行在集群中的每一个节点上（以守护进程的形式部署）。Cilium CNI 插件执行所有与网络管道有关的任务，如创建链接设备（veth 对），为容器分配 IP，配置 IP 地址，路由表，sysctl 参数等。Cilium Agent 编译 BPF 程序，并使内核在网络栈的关键点上运行这些程序。</p>
<p>Cilium 提供两种联网模式：</p>
<ul>
<li>叠加网络（）Overlay）模式：Cilium 默认的网络模式。集群中的所有节点为一个网状的隧道，使用基于 udp 的封装协议。VXLAN（默认）或 Geneve （通用网络虚拟化封装）。在这种模式下，Cilium 可以自动形成一个覆盖网络，无需用户使用 kube-controller-manager 中的 <code>--allocate-node-cidrs</code> 选项进行任何配置。</li>
<li>直接/本地路由模式：在这个配置中，Cilium 会把所有不针对另一个本地端点的数据包交给 linux 内核的路由子系统。这个设置需要一个额外的路由守护程序，如 Bird、Quagga、BGPD、Zebra 等，通过节点的 IP 向所有其他节点公布非本地节点分配的前缀。与 VxLAN 叠加相比，BGP 方案具有更好的性能，更重要的是，它使容器 IP 可路由化，无需任何额外的网状配置。</li>
</ul>
<p>Cilium 在主机网络空间上创建了三个虚拟接口：cilium<em>host、cilium</em>net 和 cilium<em>vxlan。Cilium Agent 在启动时创建一个名为“cilium</em>host -&gt; cilium<em>net”的 veth 对，并将 CIDR 的第一个 IP 地址设置为 cilium</em>host，然后作为 CIDR 的网关。CNI 插件会生成 BPF 规则，编译后注入内核，以解决 veth 对之间的连通问题。数据链路参考如下：</p>
<p><img src="assets/30eb18f0-0c9b-11eb-bf86-c1f111c841d1.jpg" alt="14-2-cilium-cni-kube-impl" /></p>
<h3>落地安装实践</h3>
<p>因为 Cilium 对内核要求很高，本来我以为需要采用 Ubuntu 才可以安装，后来查阅文档发现，只要是 CentOS 7.x 之后就可以支持。安装步骤如下。</p>
<ol>
<li>先挂载 bpf 模块：</li>
</ol>
<pre><code>sudo mount bpffs -t bpf /sys/fs/bpf

</code></pre>
<ol start="2">
<li>修改 /etc/fstab 文件，在最后面加入如下配置：</li>
</ol>
<pre><code>bpffs                  /sys/fs/bpf             bpf     defaults 0 0

</code></pre>
<ol start="3">
<li>安装一套干净的 Kubernetes 系统，这里我采用 K3s 快速搭建：</li>
</ol>
<pre><code>export MASTER_IP=$(ip a |grep global | grep -v '10.0.2.15' | awk '{print $2}' | cut -f1 -d '/')
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC=&quot;--flannel-backend=none --no-flannel --node-ip=${MASTER_IP} --node-external-ip=${MASTER_IP} --bind-address=${MASTER_IP} --no-deploy servicelb --no-deploy traefik&quot; sh -

</code></pre>
<ol start="4">
<li>在这之后，当你运行以下命令，你应该看到 local-path，metrics-server 和 coredns pods 处于 Pending 状态。这是正常的。</li>
</ol>
<pre><code>[<a href="../../cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="9ae8f5f5eedafeffecb7f7f4fdb7eefff7ea">[email&#160;protected]</a> ~]# kubectl get po -n kube-system
NAME                                     READY   STATUS    RESTARTS   AGE
coredns-7944c66d8d-xn96v                 0/1     Pending   0          3m2s
local-path-provisioner-6d59f47c7-77bfz   0/1     Pending   0          3m2s
metrics-server-7566d596c8-8bhrq          0/1     Pending   0          3m2s

</code></pre>
<ol start="5">
<li>安装 helm3：</li>
</ol>
<pre><code>sudo wget — no-check-certificate https://get.helm.sh/helm-v3.2.4-linux-amd64.tar.gz
sudo tar -zxvf helm-v3.2.4-linux-amd64.tar.gz
sudo mv linux-amd64/helm /usr/local/bin/helm

</code></pre>
<ol start="6">
<li>安装 Cilium 套件：</li>
</ol>
<pre><code># sudo helm repo add cilium https://helm.cilium.io/

# sudo helm install cilium cilium/cilium --set global.device=eth0 --set global.tag=&quot;v1.8.1&quot; \
--set global.containerRuntime.integration=&quot;containerd&quot; \
--set global.containerRuntime.socketPath=&quot;/var/run/k3s/containerd/containerd.sock&quot; \
--set global.kubeProxyReplacement=&quot;strict&quot; \
--set global.hubble.enabled=&quot;true&quot; \
--set global.hubble.listenAddress=&quot;:4244&quot; \
--set global.hubble.metrics.enabled=&quot;{dns,drop,tcp,flow,port-distribution,icmp,http}&quot; \
--set global.hubble.relay.enabled=&quot;true&quot; \
--set global.hubble.ui.enabled=&quot;true&quot; \
--kubeconfig /etc/rancher/k3s/k3s.yaml --namespace kube-system

NAME: cilium
LAST DEPLOYED: Fri Oct  9 19:53:59 2020
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
You have successfully installed Cilium with Hubble Relay and Hubble UI.

Your release version is 1.8.4.

For any further help, visit https://docs.cilium.io/en/v1.8/gettinghelp

</code></pre>
<ol start="7">
<li>去掉 IPAM 特性：</li>
</ol>
<pre><code>kubectl edit configmap cilium-config -n kube-system

### 把以下配置去掉
  ipam: cluster-pool
  k8s-require-ipv4-pod-cidr: &quot;true&quot;
  k8s-require-ipv6-pod-cidr: &quot;false&quot;

</code></pre>
<p>稍等片刻，就可以看到 Cilium 相关的容器都启动起来了。Cilium 容器网络配置成功。</p>
<ol start="8">
<li>修改 Hubble UI 控制台服务为 NodePort 模式：</li>
</ol>
<pre><code>sudo kubectl edit svc hubble-ui -n kube-system

sudo kubectl get svc hubble-ui -n kube-system

</code></pre>
<p>然后就可以查看可视化数据平台，如下图：</p>
<p><img src="assets/649f0760-0c9b-11eb-b059-25b81b32ffa7.jpg" alt="14-3-hubble-ui" /></p>
<h3>经验总结</h3>
<p>Cilium 网络方案从实际体验来看，已经可以满足常规容器网络需求。它的可视化控制台 Hubble 是对数据平面可视化的最原生实现，比 Istio 的方案显然要技高一筹。数据可视化这块让笔者有点意外，没有想到 eBPF 的编程能力可以这么强，为之后更多的插件功能带来更多期待。因为 cilium 技术太新，按照实践经验，笔者推荐大家在开发测试环境可以大胆使用起来，生产环境还要再等等，我相信在经过半年的磨砺，Cilium 应该会成为 Kubernetes 社区使用最多的容器网络方案。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;Service&#32;层引流技术实践.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;应用流量的优雅无损切换实践.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script data-cfasync="false" src="../../cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346983a0270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
