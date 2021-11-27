<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13 理解对方暴露服务的对象 Ingress 和 Service.md</title>
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

                    <a class="current-tab" href="13&#32;理解对方暴露服务的对象&#32;Ingress&#32;和&#32;Service.md">13 理解对方暴露服务的对象 Ingress 和 Service.md</a>
                    

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
                        <div><h1>13 理解对方暴露服务的对象 Ingress 和 Service</h1>
<p>Kubernetes 中的服务（Service）可以理解为对外暴露服务的最小单元对象，这个和 Pod 对象还是有不同的。例如用户通过发布服务对象 Deployment 发布应用，当在容器集群中启动后，ReplicaSet 副本对象会帮我们维持 Pod 实例的副本数。Pod 使用的容器网络默认会选择构建在主机网络上的覆盖网络（Overlay），默认外网是无法直接访问这些 Pod 实例服务的。为了能有效对接容器网络，Kubernetes 创建了另外一层虚拟网络 ClusterIP，即 Service 对象。从实现上来看，它借助 iptables 调用底层 netfilter 实现了虚拟 IP，然后通过相应的规则链把南北向流量准确无误的接入后端 Pod 实例。随着需求的衍生，后来扩展的 Ingress 对象则是借助第三方代理服务如 HAProxy、Nginx 等 7 层引流工具打通外部流量和内部 Service 对象的通路。Ingress 对象的目的就是为了解决容器集群中需要高性能应用网关接入的需求。</p>
<h3>Service 的思考</h3>
<p>Service 定义的网络基于 iptables 编排 netfilter 规则来支持虚拟 IP。Service 对象被设计为反向代理模式，支持南北向流量的负载均衡，通过 DNAT 把流量转到后端的具体业务的 Pod 中。为了劫持接入流量和 NAT 转换，Kubernetes 创建了两条自定义链规则 PREROUTING 和 OUTPUT。如：</p>
<pre><code>-A PREROUTING -m comment --comment &quot;kubernetes service portals&quot; -j KUBE-SERVICES
...
-A OUTPUT -m comment --comment &quot;kubernetes service portals&quot; -j KUBE-SERVICES
...

</code></pre>
<p>PREROUTING 主要处理从外部引入的流量和来自 Pod 容器网络的引入流量，OUTPUT 主要处理流出到外部网络的流量和流出到 Pod 容器网络的流量。</p>
<p>因为发布的服务肯定需要对外暴露服务，所以 Kubernetes 创建了一个自定义规则链 KUBE-SERVICE 来支持集群级别的服务发现，即 ClusterIP 和 LoadBalancer 类型，最后通过另外一条自定义规则链 KUBE-NODEPORTS 来对外暴露服务，案例如下：</p>
<pre><code>-A KUBE-SERVICES -m comment --comment &quot;kubernetes service nodeports; NOTE: this must be the last rule in this chain&quot; -m addrtype --dst-type LOCAL -j KUBE-NODEPORTS

</code></pre>
<p>每一个 Service 都会创建一套规则链，NODEPORTS 规则必须在最后一行。因此不难知道，当服务数量达到上万个时候，iptables 是无法承载这种规模的规则链的处理的。所以，在最新服务方案中默认引入 ipvs 取代 iptables 的原因。</p>
<h4><strong>ClusterIP 类型</strong></h4>
<p>Service 默认类型，配合场景可以分为以下 5 种分类：</p>
<ul>
<li>ClusterIP service</li>
<li>ClusterIP service with session affinity</li>
<li>ClusterIP with external IPs</li>
<li>ClusterIP service without any endpoints</li>
<li>Headless service</li>
</ul>
<p>为了加深印象，以下通过案例来学习 Service 对象：</p>
<pre><code>#redis.yaml
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: redis
spec:
  replicas: 2
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis
        ports:
        - containerPort: 6379
          name: redis

</code></pre>
<p>先创建普通的 Service：</p>
<pre><code>#redis-clusterip.yaml
apiVersion: v1
kind: Service
metadata:
  name: redis
spec:
  ports:
  - port: 6379
  selector:
    app: redis

</code></pre>
<p>查看 Service 情况：</p>
<pre><code>#kubectl get service redis
NAME    TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
redis   ClusterIP   10.0.19.85   &lt;none&gt;        6379/TCP   3d4h

#kubectl get endpoints redis
NAME    ENDPOINTS                           AGE
redis   10.244.1.69:6379,10.244.1.70:6379   3d4h

</code></pre>
<p>很多用户在遇到这个 Cluster ip 后，就会尝试 ping 它，但是 ping 不通，也不清楚为什么。其实它是一个虚拟 IP，并没有相关网络进程和它关联，当然也就无法访问。Kubernetes 默认会在创建 Service 的时候把此虚拟 IP 加入到内置的 DNS 中用来支持服务发现，仅此而已。如下：</p>
<pre><code>#nslookup redis.default.svc.cluster.local 10.0.0.10
Server:        10.0.0.10
Address:    10.0.0.10#53

Name:    redis.default.svc.cluster.local
Address: 10.0.19.85

</code></pre>
<p>现在查看 kube-proxy 通过 iptables 定义的规则链，了解流量接入的实现方法如下：</p>
<pre><code>-A KUBE-SERVICES ! -s 10.244.0.0/16 -d 10.0.19.85/32 -p tcp -m comment --comment &quot;default/redis: cluster IP&quot; -m tcp --dport 6379 -j KUBE-MARK-MASQ
-A KUBE-SERVICES -d 10.0.19.85/32 -p tcp -m comment --comment &quot;default/redis: cluster IP&quot; -m tcp --dport 6379 -j KUBE-SVC-SCFPZ36VFLUNBB47

-A KUBE-SVC-SCFPZ36VFLUNBB47 -m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-UH5EYFQKYB24RWKN
-A KUBE-SVC-SCFPZ36VFLUNBB47 -j KUBE-SEP-5MXPM55VLN7O52FQ

-A KUBE-SEP-UH5EYFQKYB24RWKN -s 10.244.1.69/32 -j KUBE-MARK-MASQ
-A KUBE-SEP-UH5EYFQKYB24RWKN -p tcp -m tcp -j DNAT --to-destination 10.244.1.69:6379

-A KUBE-SEP-5MXPM55VLN7O52FQ -s 10.244.1.70/32 -j KUBE-MARK-MASQ
-A KUBE-SEP-5MXPM55VLN7O52FQ -p tcp -m tcp -j DNAT --to-destination 10.244.1.70:6379

</code></pre>
<p>注意，Service 这层的负载均衡是通过 iptables 的 statistic 模块实现：</p>
<pre><code>-A KUBE-SVC-SCFPZ36VFLUNBB47 -m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-UH5EYFQKYB24RWKN
-A KUBE-SVC-SCFPZ36VFLUNBB47 -j KUBE-SEP-5MXPM55VLN7O52FQ

</code></pre>
<p>还有一个问题，就是 Pod 内网 IP 访问 Service IP 的时候是会发生端口流量回流的。如何让端口流量不回流的技术，专业术语叫 hairpin NAT。通过 kubelet 配置参数 <code>--hairpin-mode=hairpin-veth</code> 可以让 Pod 内网网卡自动支持 hairpin，从而解决虚拟网卡流量回流的问题。</p>
<p>让 ClusterIP 支持流量亲和性，你需要如下声明对象：</p>
<pre><code>#redis-clusterip-sa.yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-sa
spec:
  sessionAffinity: ClientIP
  ports:
  - port: 6379
  selector:
    app: redis

</code></pre>
<p>查看 iptables 生成的规则如下：</p>
<pre><code>-A KUBE-SERVICES ! -s 10.244.0.0/16 -d 10.0.219.234/32 -p tcp -m comment --comment &quot;default/redis-sa: cluster IP&quot; -m tcp --dport 6379 -j KUBE-MARK-MASQ
-A KUBE-SERVICES -d 10.0.219.234/32 -p tcp -m comment --comment &quot;default/redis-sa: cluster IP&quot; -m tcp --dport 6379 -j KUBE-SVC-YUZPDSCUOF7FG5LD

-A KUBE-SVC-YUZPDSCUOF7FG5LD -m recent --rcheck --seconds 10800 --reap --name KUBE-SEP-6MUUJB4K75LGZXHS --mask 255.255.255.255 --rsource -j KUBE-SEP-6MUUJB4K75LGZXHS
-A KUBE-SVC-YUZPDSCUOF7FG5LD -m recent --rcheck --seconds 10800 --reap --name KUBE-SEP-F5DCISRHJOTG66JA --mask 255.255.255.255 --rsource -j KUBE-SEP-F5DCISRHJOTG66JA
-A KUBE-SVC-YUZPDSCUOF7FG5LD -m statistic --mode random --probability 0.50000000000 -j KUBE-SEP-6MUUJB4K75LGZXHS
-A KUBE-SVC-YUZPDSCUOF7FG5LD -j KUBE-SEP-F5DCISRHJOTG66JA

-A KUBE-SEP-6MUUJB4K75LGZXHS -s 10.244.1.69/32 -j KUBE-MARK-MASQ
-A KUBE-SEP-6MUUJB4K75LGZXHS -p tcp -m recent --set --name KUBE-SEP-6MUUJB4K75LGZXHS --mask 255.255.255.255 --rsource -m tcp -j DNAT --to-destination 10.244.1.69:6379

-A KUBE-SEP-F5DCISRHJOTG66JA -s 10.244.1.70/32 -j KUBE-MARK-MASQ
-A KUBE-SEP-F5DCISRHJOTG66JA -p tcp -m recent --set --name KUBE-SEP-F5DCISRHJOTG66JA --mask 255.255.255.255 --rsource -m tcp -j DNAT --to-destination 10.244.1.70:6379

</code></pre>
<p>通过以上的规则链，可以知道链路亲和性主要是通过 iptables 的 recent 模块来支持的。</p>
<p>如果不想创建 ClusterIP，可以声明 None 去掉 ClusterIP 支持，如下：</p>
<pre><code>#redis-clusterip-headless.yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-headless
spec:
  clusterIP: None
  ports:
  - port: 6379
  selector:
    app: redis

</code></pre>
<p>通过内网 DNS 可以了解到，查询 Service 将直接列出 Pod 的 IP 了，如下：</p>
<pre><code>#nslookup redis-headless.default.svc.cluster.local 10.0.0.10
Server:        10.0.0.10
Address:    10.0.0.10#53

Name:    redis-headless.default.svc.cluster.local
Address: 10.244.1.69
Name:    redis-headless.default.svc.cluster.local
Address: 10.244.1.70

</code></pre>
<h4><strong>NodePort 类型</strong></h4>
<p>NodePort 类型也是我们最常用的类型，按照场景分类如下 5 种：</p>
<ul>
<li>NodePort service</li>
<li>NodePort service with externalTrafficPolicy: Local</li>
<li>NodePort service without any endpoints</li>
<li>NodePort service with session affinity</li>
<li>NodePort service with externalTrafficPolicy: Local and session affinity</li>
</ul>
<p>一般常见的定义如下：</p>
<pre><code>#redis-nodeport.yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-nodeport
spec:
  type: NodePort
  ports:
  - nodePort: 30001
    port: 6379
    targetPort: 6379    
  selector:
    app: redis

</code></pre>
<p>查看创建结果如下：</p>
<pre><code>#kubectl get service redis-nodeport
NAME             TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
redis-nodeport   NodePort   10.0.118.143   &lt;none&gt;        6379:30001/TCP   107s

#kubectl get endpoints redis-nodeport
NAME             ENDPOINTS          AGE
redis-nodeport   10.244.0.4:6379   110s

</code></pre>
<p>通过暴露在主机层面的 30001 端口，外网可以轻松访问到容器集群中的服务。</p>
<h3>Ingress 的思考</h3>
<p>Ingress 打通了从集群外部到集群内服务的 HTTP 和 HTTPS 路由。流量路由由 Ingress 资源上定义的规则控制。其实真正的流量负载由第三方代理服务来支撑，如 HAProxy。大家可以回顾一下，在没有 Ingress 之前，我们一般都会在集群外部部署接入网关，然后把流量引入集群。但是 Kubernetes 集群中的服务是动态的，如何能通过查询 APIServer 动态获得服务列表和端口，然后实时更新到网关中，这不就完美实现业务需求了吗？是的，Ingress 因此而生，它的主要能力就是为服务提供外部可访问的 URL、负载均衡流量、终止 SSL/TLS。</p>
<p>通过一个最小的 Ingress 资源示例来熟悉下：</p>
<pre><code>apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: test-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - path: /testpath
        pathType: Prefix
        backend:
          serviceName: test
          servicePort: 80

</code></pre>
<p>Nginx 的规则更新主要是通过 nginx-controller 定期从 APIServer 中抓取获得。</p>
<h4><strong>特性一：服务分组</strong></h4>
<p>一个分组配置根据请求的 HTTP URI 将流量从单个 IP 地址路由到多个服务。Ingress 允许将负载均衡器的数量降至最低。例如，这样的设置：</p>
<pre><code>foo.bar.com -&gt; 178.91.123.132 -&gt; / foo    service1:4200
                                 / bar    service2:8080

</code></pre>
<h4><strong>特性二：基于名称的虚拟托管</strong></h4>
<p>基于名称的虚拟域名支持将针对多个主机名的 HTTP 流量路由到同一 IP 地址上。</p>
<pre><code>foo.bar.com --|                 |-&gt; foo.bar.com service1:80
              | 178.91.123.132  |
bar.foo.com --|                 |-&gt; bar.foo.com service2:80

</code></pre>
<h4><strong>特性三：TLS 终止</strong></h4>
<p>通过设定包含 TLS 私钥和证书的 Secret 来保护 Ingress。目前，Ingress 只支持单个 TLS 端口 443，并假定 TLS 终止。</p>
<pre><code>apiVersion: v1
kind: Secret
metadata:
  name: testsecret-tls
  namespace: default
data:
  tls.crt: base64 encoded cert
  tls.key: base64 encoded key
type: kubernetes.io/tls

</code></pre>
<p>在 Ingress 中引用此 Secret 将会告诉 Ingress 控制器使用 TLS 加密从客户端到负载均衡器的通道。你需要确保创建的 TLS Secret 来自包含 sslexample.foo.com 的公用名称（CN）的证书。这里的公共名称也被称为全限定域名（FQDN）。</p>
<pre><code>apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: tls-example-ingress
spec:
  tls:
  - hosts:
    - sslexample.foo.com
    secretName: testsecret-tls
  rules:
    - host: sslexample.foo.com
      http:
        paths:
        - path: /
          backend:
            serviceName: service1
            servicePort: 80

</code></pre>
<p>从案例中来看，Ingress 虽然承担这应用网关的职责，但是其设计的能力受制于第三方代理组件，反而没有自定义应用网关那么灵活。所以在具体业务中，我们仍然需要考量需求后在觉得是否需要引入 Ingress。</p>
<h3>总结</h3>
<p>集群对外服务对象 Service 和 Ingress 往往被人误解，并和 Pod 服务发现混在一起。通过以上的案例分析，我们可以充分理解 Service 的实现。从实践中发现，Service 这层的作用是起到承上启下的入口作用，功能上只要能暴露主机端口 NodePort 即可。采用 iptables 实现的 NAT 转换只有在上万规模服务的时候，规则链的暴增才会影响性能，采用 ipvs 反向代理模块后可以缓解。但是 iptables 定义的规则链还要解决 Service 和 Pod 容器网络的 NAT 连通，目前还无法完全去掉 iptables 模块。随着 eBPF 的兴起，预计后面去 iptables 化指日可待。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;练习篇：K8s&#32;集群配置测验.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;应用网关&#32;OpenResty&#32;对接&#32;K8s&#32;实践.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434685add970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
