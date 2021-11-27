<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>22 服务增强：Ingress.md</title>
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

                    <a class="current-tab" href="22&#32;服务增强：Ingress.md">22 服务增强：Ingress.md</a>
                    

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
                        <div><h1>22 服务增强：Ingress</h1>
<h2>整体概览</h2>
<p>通过前面的学习，我们已经知道 K8S 中有 <code>Service</code> 的概念，同时默认情况下还有 <code>CoreDNS</code> 完成集群内部的域名解析等工作，以此完成基础的服务注册发现能力。</p>
<p>在第 7 节中，我们介绍了 <code>Service</code> 的 4 种基础类型，在前面的介绍中，我们一般都在使用 <code>ClusterIP</code> 或 <code>NodePort</code> 等方式将服务暴露在集群内或者集群外。</p>
<p>本节，我们将介绍另一种处理服务访问的方式 <code>Ingress</code>。</p>
<h2>Ingress 是什么</h2>
<p>通过 <code>kubectl explain ingress</code> 命令，我们来看下对 Ingress 的描述。</p>
<blockquote>
<p>Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.</p>
</blockquote>
<p><code>Ingress</code> 是一组允许外部请求进入集群的路由规则的集合。它可以给 <code>Service</code> 提供集群外部访问的 URL，负载均衡，SSL 终止等。</p>
<p>直白点说，<code>Ingress</code> 就类似起到了智能路由的角色，外部流量到达 <code>Ingress</code> ，再由它按已经制定好的规则分发到不同的后端服务中去。</p>
<p>看起来它很像我们使用的负载均衡器之类的。那你可能会问，<code>Ingress</code> 与 <code>LoadBalancer</code> 类型的 <code>Service</code> 的区别是什么呢？</p>
<ul>
<li>
<p><code>Ingress</code> 不是一种 <code>Service</code> 类型</p>
<p><code>Ingress</code> 是 K8S 中的一种资源类型，我们可以直接通过 <code>kubectl get ingress</code> 的方式获取我们已有的 <code>Ingress</code> 资源。</p>
</li>
<li>
<p><code>Ingress</code> 可以有多种控制器（实现）</p>
<p>通过之前的介绍，我们知道 K8S 中有很多的 <code>Controller</code> (控制器)，而这些 <code>Controller</code> 已经打包进了 <code>kube-controller-manager</code> 中，通过 <code>--controllers</code> 参数控制启用哪些。</p>
<p>但是 <code>Ingress</code> 的 <code>Controller</code> 并没有包含在其中，而且有多种选择。</p>
<p>由社区维护（或是说官方支持的）有两个：适用于 Google Cloud 的 <a href="https://github.com/kubernetes/ingress-gce">GLBC</a>，当你使用 GKE 的时候，便会看到它；和 <a href="https://github.com/kubernetes/ingress-nginx">NGINX Ingress Controller</a> 它是使用 <code>ConfigMap</code> 存储 NGINX 配置实现的。</p>
<p>第三方的实现还有：基于 Envoy 的 <a href="https://github.com/heptio/contour">Contour</a>; F5 的 <a href="https://clouddocs.f5.com/products/connectors/k8s-bigip-ctlr/v1.7/">F5 BIG-IP Controller</a>; 基于 HAProxy 的 <a href="https://github.com/jcmoraisjr/haproxy-ingress">haproxy-ingress</a>; 基于 Istio 的 <a href="https://istio.io/docs/tasks/traffic-management/ingress/">Control Ingress Traffic</a>; 现代化的反向代理服务器 <a href="https://github.com/containous/traefik">Traefik</a>; 以及 Kong 支持的 <a href="https://konghq.com/blog/kubernetes-ingress-controller-for-kong/">Kong Ingress Controller for Kubernetes</a> 和 NGINX 官方支持的 <a href="https://github.com/nginxinc/kubernetes-ingress">NGINX Ingress Controller</a>。</p>
<p>这里可以看到 K8S 社区和 NGINX 都有 NGINX Ingress Controller，很多人在一开始接触 Ingress 的时候便陷入了选择的苦恼中，除去前面的那些选择外，单 NGINX 的控制器就有两个，到底应该怎么选。</p>
<p>这里提供两点建议：</p>
<ul>
<li>可能多数人使用的都是 NGINX 而非 NGINX Plus，如果你需要会话保持（Session persistence）的话，那你应该选择 K8S 社区维护的版本</li>
<li>即使我们平时使用 NGINX 的时候，也常常会有动态配置的需求，如果你仍然有这样的需求，那你还是继续使用 K8S 社区维护的版本（其中内置了 Lua 支持）。</li>
</ul>
</li>
</ul>
<h2>如何使用</h2>
<p>前面也已经说到了，单纯的创建一个 <code>Ingress</code> 资源没什么意义，我们需要先配置一个 <code>Controller</code> ，才能让它正常工作。国内使用 GKE 的可能不是很多，为了更加通用，这里我们选择 K8S 社区维护的 NGINX Ingress Controller。</p>
<h3>安装</h3>
<p>整个安装过程其实也比较简单，具体步骤如下（以下步骤中都将直接展示该步骤所需的 YAML 配置文件）：</p>
<ul>
<li>
<p>创建 <code>Namespace</code></p>
<pre><code>apiVersion: v1
kind: Namespace
metadata:
  name: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
</code></pre>
<p>将以上内容保存为 namespace.yaml 文件，然后执行 <code>kubectl apply -f namespace.yaml</code> 即可。以下步骤均类似，不再赘述。 注意：这里创建 <code>Namespace</code> 只是为了保持集群相对规范，非强制，但推荐此做法。</p>
</li>
<li>
<p>创建 <code>ConfigMap</code></p>
<pre><code>kind: ConfigMap
apiVersion: v1
metadata:
  name: nginx-configuration
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx

---
kind: ConfigMap
apiVersion: v1
metadata:
  name: tcp-services
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx

---
kind: ConfigMap
apiVersion: v1
metadata:
  name: udp-services
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx

---
</code></pre>
<p>这里创建了几个 <code>ConfigMap</code>，主要是给 <code>Controller</code> 使用。</p>
</li>
<li>
<p>由于我们的集群使用 <code>kubeadm</code> 创建时，默认开启了 <code>RBAC</code> ，所以这里需要相应的创建对应的 <code>Role</code> 和 <code>RoleBinding</code>。</p>
<pre><code>apiVersion: v1
kind: ServiceAccount
metadata:
  name: nginx-ingress-serviceaccount
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx

---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRole
metadata:
  name: nginx-ingress-clusterrole
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
rules:
  - apiGroups:
      - &quot;&quot;
    resources:
      - configmaps
      - endpoints
      - nodes
      - pods
      - secrets
    verbs:
      - list
      - watch
  - apiGroups:
      - &quot;&quot;
    resources:
      - nodes
    verbs:
      - get
  - apiGroups:
      - &quot;&quot;
    resources:
      - services
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - &quot;extensions&quot;
    resources:
      - ingresses
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - &quot;&quot;
    resources:
      - events
    verbs:
      - create
      - patch
  - apiGroups:
      - &quot;extensions&quot;
    resources:
      - ingresses/status
    verbs:
      - update

---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: Role
metadata:
  name: nginx-ingress-role
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
rules:
  - apiGroups:
      - &quot;&quot;
    resources:
      - configmaps
      - pods
      - secrets
      - namespaces
    verbs:
      - get
  - apiGroups:
      - &quot;&quot;
    resources:
      - configmaps
    resourceNames:
      - &quot;ingress-controller-leader-nginx&quot;
    verbs:
      - get
      - update
  - apiGroups:
      - &quot;&quot;
    resources:
      - configmaps
    verbs:
      - create
  - apiGroups:
      - &quot;&quot;
    resources:
      - endpoints
    verbs:
      - get

---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: RoleBinding
metadata:
  name: nginx-ingress-role-nisa-binding
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: nginx-ingress-role
subjects:
  - kind: ServiceAccount
    name: nginx-ingress-serviceaccount
    namespace: ingress-nginx

---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: nginx-ingress-clusterrole-nisa-binding
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: nginx-ingress-clusterrole
subjects:
  - kind: ServiceAccount
    name: nginx-ingress-serviceaccount
    namespace: ingress-nginx

---
</code></pre>
<p>关于 <code>RBAC</code> 相关的内容，可查看第 8 节 《安全重点: 认证和授权》，了解此处的配置及其含义。</p>
</li>
<li>
<p>部署 NGINX Ingress Controller</p>
<pre><code>apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-ingress-controller
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: ingress-nginx
      app.kubernetes.io/part-of: ingress-nginx
  template:
    metadata:
      labels:
        app.kubernetes.io/name: ingress-nginx
        app.kubernetes.io/part-of: ingress-nginx
      annotations:
        prometheus.io/port: &quot;10254&quot;
        prometheus.io/scrape: &quot;true&quot;
    spec:
      serviceAccountName: nginx-ingress-serviceaccount
      containers:
        - name: nginx-ingress-controller
          image: taobeier/nginx-ingress-controller:0.21.0
          args:
            - /nginx-ingress-controller
            - --configmap=$(POD_NAMESPACE)/nginx-configuration
            - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
            - --udp-services-configmap=$(POD_NAMESPACE)/udp-services
            - --publish-service=$(POD_NAMESPACE)/ingress-nginx
            - --annotations-prefix=nginx.ingress.kubernetes.io
          securityContext:
            capabilities:
              drop:
                - ALL
              add:
                - NET_BIND_SERVICE
            # www-data -&gt; 33
            runAsUser: 33
          env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
          ports:
            - name: http
              containerPort: 80
            - name: https
              containerPort: 443
          livenessProbe:
            failureThreshold: 3
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
</code></pre>
<p>注意，这里的镜像是我从官方镜像直接同步的，为了解决国内无法下载镜像的情况。</p>
<p>另外，在启动参数中，指定了我们第二步中创建的 <code>ConfigMap</code> 。以及，在此部署中，用到了之前尚未详细说明的 <code>readinessProbe</code> 和 <code>livenessProbe</code>：我们之前在详解 <code>kubelet</code> 时，大致提到过关于它所具备的职责，这两个配置主要是用于做探针，用户检查 Pod 是否已经准备好接受请求流量和是否存活。</p>
<p>这里还进行了 <code>annotations</code> 里面标注了关于 <code>Prometheus</code> 的相关内容，我们会在下节中描述。</p>
<pre><code>master $ kubectl -n ingress-nginx get all
NAME                                            READY     STATUS    RESTARTS   AGE
pod/nginx-ingress-controller-6f647f7866-659ph   1/1       Running   0          75s

NAME                                       DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-ingress-controller   1         1         1            1           75s

NAME                                                  DESIRED   CURRENT   READY     AGE
replicaset.apps/nginx-ingress-controller-6f647f7866   1         1         1         75s
</code></pre>
<p>可以看到 NGINX Ingress Controller 已经部署成功。</p>
</li>
<li>
<p><strong>将 NGINX Ingress Controller 暴露至集群外</strong></p>
<p>经过前面的介绍，我们已经知道 Ingress 的作用在于将集群外的请求流量转向集群内的服务，而我们知道，默认情况下集群外和集群内是不互通的，所以必须将 NGINX Ingress Controller 暴露至集群外，以便让其能接受来自集群外的请求。</p>
<p>将其暴露的方式有很多种，这里我们选择我们之前已经介绍过的 <code>NodePort</code> 的方式。选择它主要有以下原因：</p>
<ul>
<li>我们可以使用纯的 LB 实现完成服务暴露，比如 <a href="https://metallb.universe.tf/">MetalLB</a>，但它还处于 Beta 阶段，尚未有大规模生产环境使用的验证。</li>
<li>我们可以直接使用宿主机的网络，只需设置 <code>hostNetwork: true</code> 即可，但这个方式可能会带来安全问题。</li>
<li>我们可以选择 External IPs 的方式，但这种方式无法保留请求的源 IP，所以并不是很好。</li>
<li>其实我们一般会选择自己提供边缘节点的方式，不过这种方式是建立在 <code>NodePort</code> 的方式之上，并且需要提供额外的组件，此处就暂不做展开了。</li>
</ul>
<p>我们使用以下的配置，将 NGINX Ingress Controller 暴露至集群外</p>
<pre><code>apiVersion: v1
kind: Service
metadata:
  name: ingress-nginx
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
spec:
  type: NodePort
  ports:
    - name: http
      port: 80
      targetPort: 80
      protocol: TCP
    - name: https
      port: 443
      targetPort: 443
      protocol: TCP
  selector:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
</code></pre>
<p>创建该 <code>Service</code>。</p>
<pre><code>master $ kubectl -n ingress-nginx get svc                                                  
NAME            TYPE       CLUSTER-IP   EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx   NodePort   10.0.38.53   &lt;none&gt;        80:30871/TCP,443:30356/TCP   11s
</code></pre>
<p>现在，我们直接访问 <code>Node:Port</code> 便可访问到该 Controller。</p>
<pre><code>master $ curl 172.17.0.3:30871                    
&lt;html&gt;
&lt;head&gt;&lt;title&gt;404 Not Found&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
&lt;center&gt;&lt;h1&gt;404 Not Found&lt;/h1&gt;&lt;/center&gt;
&lt;hr&gt;&lt;center&gt;nginx/1.15.6&lt;/center&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre>
<p>由于我们并没有设置任何的默认响应后端，所以当直接请求时，便返回 404 。</p>
</li>
</ul>
<h3>实践</h3>
<p>将我们的示例项目 <a href="https://github.com/tao12345666333/saythx">SayThx</a> 通过 <code>Ingress</code> 的方式进行访问。</p>
<p>该示例项目的部署，不再进行赘述。可在 <a href="https://github.com/tao12345666333/saythx/blob/ingress/deploy/ingress.yaml">ingress 分支</a> 查看此处所需配置。</p>
<p>在我们将 NGINX Ingress Controller 及 SayThx 项目部署好之后，我们使用以下的配置创建 <code>Ingress</code> 资源。</p>
<pre><code>apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: saythx-ing
  namespace: work
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: &quot;false&quot;
spec:
  rules:
  - host: saythx.moelove.info
    http:
      paths:
      - path: /
        backend:
          serviceName: saythx-frontend
          servicePort: 80
</code></pre>
<ul>
<li>
<p>创建</p>
<pre><code>master $ kubectl apply -f ingress.yaml         
ingress.extensions/saythx-ing created
master $ kubectl -n work get ing
NAME         HOSTS                 ADDRESS   PORTS     AGE
saythx-ing   saythx.moelove.info             80        23s
</code></pre>
</li>
<li>
<p>验证</p>
<p>这里来解释下刚才的配置文件。首先，指定了 <code>host: saythx.moelove.info</code> 表示我们想要以 <code>saythx.moelove.info</code> 这个域名来访问它。<code>path</code> 直接写 <code>/</code> 表示所有的请求都转发至名为 <code>saythx-frontend</code> 的服务。</p>
<p>与我们平时使用 NGINX 基本一致。 现在编辑本地的 HOSTS 文件绑定 Node 的IP 与 <code>saythx.moelove.info</code> 这个域名。使用浏览器进行访问 <code>saythx.moelove.info:刚才 Controller 使用 NodePort 暴露服务时的端口</code>：</p>
</li>
</ul>
<p><img src="assets/167dc55e62bc0a88" alt="img" /></p>
<pre><code>可以看到已经成功访问。
</code></pre>
<h2>总结</h2>
<p>在本节中，我们介绍了 <code>Ingress</code> 的基本情况，了解了它是 K8S 中的一种资源对象，主要负责将集群外部流量与集群内服务的通信。但它的正常工作离不开 <code>Ingress Controller</code> ，当前官方团队维护的主要有两个 GLBC 和 NGINX Ingress Controller。</p>
<p>我们大致介绍了现有的 Controller 实现，也实践了如何部署 NGINX Ingress Controller 以及如何使用 Ingress 将我们的示例项目暴露至集群外。</p>
<p>NGINX Ingress Controller 的使用，比较符合我们平时使用 NGINX 的习惯，相对来说也比较灵活，后续可看实际情况再进行更多的实践。</p>
<p>至此，K8S 集群的管理，相关原理以及服务的部署等内容就基本介绍完毕。下节，我们将介绍生产实践中至关重要的一环 <strong>监控</strong> 相关的实践。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="21&#32;扩展增强：CoreDNS.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="23&#32;监控实践：对&#32;K8S&#32;集群进行监控.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346323da070ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
