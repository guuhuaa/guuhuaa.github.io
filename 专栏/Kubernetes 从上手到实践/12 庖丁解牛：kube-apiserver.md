<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>12 庖丁解牛：kube-apiserver.md</title>
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

                    <a class="current-tab" href="12&#32;庖丁解牛：kube-apiserver.md">12 庖丁解牛：kube-apiserver.md</a>
                    

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
                        <div><h1>12 庖丁解牛：kube-apiserver</h1>
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
<p>在第 3 节《宏观认识：整体架构》 中，我们初次认识到了 <code>kube-apiserver</code> 的存在（以下内容中将统一称之为 <code>kube-apiserver</code>），知道了它作为集群的统一入口，接收来自外部的信号和请求，并将一些信息存储至 <code>etcd</code> 中。</p>
<p>但这只是一种很模糊的说法，本节我们来具体看看 <code>kube-apiserver</code> 的关键功能以及它的工作原理。</p>
<p>注意：本节所有的源码均以 <code>v1.11.3</code> 为准 commit id <code>a4529464e4629c21224b3d52edfe0ea91b072862</code>。</p>
<h2>REST API Server</h2>
<p>先来说下 <code>kube-apiserver</code> 作为整个集群的入口，接受外部的信号和请求所应该具备的基本功能。</p>
<p>首先，它对外提供接口，可处理来自客户端（无论我们在用的 <code>kubeclt</code> 或者 <code>curl</code> 或者其他语言实现的客户端）的请求，并作出响应。</p>
<p>在第 5 节搭建集群时，我们提到要先去检查 <code>6443</code> 端口是否被占用。这样检查的原因在于 <code>kube-apiserver</code> 有个 <code>--secure-port</code> 的参数，通过这个参数来配置它将要监听在哪个端口，默认情况下是 <code>6443</code>。</p>
<p>当然，它还有另一个参数 <code>--insecure-port</code> ，这个参数可将 <code>kube-apiserver</code> 绑定到其指定的端口上，且通过该端口访问时无需认证。</p>
<p>在生产环境中，建议将其设置为 <code>0</code> 以禁用该功能。另外，这个参数也已经被标记为废弃，将在之后版本中移除。如果未禁用该功能，建议通过防火墙策略禁止从外部访问该端口。该端口会绑定在 <code>--insecure-bind-address</code> 参数所设置的地址上，默认为 <code>127.0.0.1</code>。</p>
<p>那么 <code>secure</code> 和 <code>insecure</code> 最主要的区别是什么呢？ 这就引出来了 <code>kube-apiserver</code> 作为 API Server 的一个最主要功能：认证。</p>
<h3>认证（Authentication）</h3>
<p>在第 8 节《认证和授权》中，我们已经讲过认证相关的机制。这里，我们以最简单的获取集群版本号为例。</p>
<p>通常，我们使用 <code>kubeclt version</code> 来获取集群和当前客户端的版本号。</p>
<pre><code>master $ kubectl version
Client Version: version.Info{Major:&quot;1&quot;, Minor:&quot;11&quot;, GitVersion:&quot;v1.11.3&quot;, GitCommit:&quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-09-09T18:02:47Z&quot;, GoVersion:&quot;go1.10.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
Server Version: version.Info{Major:&quot;1&quot;, Minor:&quot;11&quot;, GitVersion:&quot;v1.11.3&quot;, GitCommit:&quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-09-09T17:53:03Z&quot;, GoVersion:&quot;go1.10.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
</code></pre>
<p>获取集群版本号的时候，其实也是向 <code>kube-apiserver</code> 发送了一个请求进行查询的，我们可以通过传递 <code>-v</code> 参数来改变 log level 。</p>
<pre><code>master $ kubectl version -v 8
I1202 03:15:06.360838   13581 loader.go:359] Config loaded from file /root/.kube/config
I1202 03:15:06.362106   13581 round_trippers.go:383] GET https://172.17.0.99:6443/version?timeout=32s
I1202 03:15:06.362130   13581 round_trippers.go:390] Request Headers:
I1202 03:15:06.362139   13581 round_trippers.go:393]     Accept: application/json, */*
I1202 03:15:06.362146   13581 round_trippers.go:393]     User-Agent: kubectl/v1.11.3 (linux/amd64) kubernetes/a452946
I1202 03:15:06.377653   13581 round_trippers.go:408] Response Status: 200 OK in 15 milliseconds
I1202 03:15:06.377678   13581 round_trippers.go:411] Response Headers:
I1202 03:15:06.377686   13581 round_trippers.go:414]     Content-Type: application/json
I1202 03:15:06.377693   13581 round_trippers.go:414]     Content-Length: 263
I1202 03:15:06.377699   13581 round_trippers.go:414]     Date: Sun, 02 Dec 2018 03:15:06 GMT
I1202 03:15:06.379314   13581 request.go:897] Response Body: {
  &quot;major&quot;: &quot;1&quot;,
  &quot;minor&quot;: &quot;11&quot;,
  &quot;gitVersion&quot;: &quot;v1.11.3&quot;,
  &quot;gitCommit&quot;: &quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;,
  &quot;gitTreeState&quot;: &quot;clean&quot;,
  &quot;buildDate&quot;: &quot;2018-09-09T17:53:03Z&quot;,
  &quot;goVersion&quot;: &quot;go1.10.3&quot;,
  &quot;compiler&quot;: &quot;gc&quot;,
  &quot;platform&quot;: &quot;linux/amd64&quot;
}
Client Version: version.Info{Major:&quot;1&quot;, Minor:&quot;11&quot;, GitVersion:&quot;v1.11.3&quot;, GitCommit:&quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-09-09T18:02:47Z&quot;, GoVersion:&quot;go1.10.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
Server Version: version.Info{Major:&quot;1&quot;, Minor:&quot;11&quot;, GitVersion:&quot;v1.11.3&quot;, GitCommit:&quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;, GitTreeState:&quot;clean&quot;, BuildDate:&quot;2018-09-09T17:53:03Z&quot;, GoVersion:&quot;go1.10.3&quot;, Compiler:&quot;gc&quot;, Platform:&quot;linux/amd64&quot;}
</code></pre>
<p>通过日志就可以很明显看到，首先会加载 <code>$HOME/.kube/config</code> 下的配置，获的集群地址，进而请求 <code>/version</code> 接口，最后格式化输出。</p>
<p>我们使用 <code>curl</code> 去请求同样的接口：</p>
<pre><code>master $ curl -k https://172.17.0.99:6443/version
{
  &quot;major&quot;: &quot;1&quot;,
  &quot;minor&quot;: &quot;11&quot;,
  &quot;gitVersion&quot;: &quot;v1.11.3&quot;,
  &quot;gitCommit&quot;: &quot;a4529464e4629c21224b3d52edfe0ea91b072862&quot;,
  &quot;gitTreeState&quot;: &quot;clean&quot;,
  &quot;buildDate&quot;: &quot;2018-09-09T17:53:03Z&quot;,
  &quot;goVersion&quot;: &quot;go1.10.3&quot;,
  &quot;compiler&quot;: &quot;gc&quot;,
  &quot;platform&quot;: &quot;linux/amd64&quot;
}
</code></pre>
<p>得到了相同的结果。你可能会有些奇怪，使用 <code>curl -k</code> 相当于忽略了认证的过程，为何还能拿到正确的信息。别急，我们来看下一个例子：</p>
<pre><code>master $ kubectl get ns  -v 8
I1202 03:25:40.607886   16620 loader.go:359] Config loaded from file /root/.kube/config
I1202 03:25:40.608862   16620 loader.go:359] Config loaded from file /root/.kube/config
I1202 03:25:40.611187   16620 loader.go:359] Config loaded from file /root/.kube/config
I1202 03:25:40.622737   16620 loader.go:359] Config loaded from file /root/.kube/config
I1202 03:25:40.623495   16620 round_trippers.go:383] GET https://172.17.0.99:6443/api/v1/namespaces?limit=500
I1202 03:25:40.623650   16620 round_trippers.go:390] Request Headers:
I1202 03:25:40.623730   16620 round_trippers.go:393]     Accept: application/json;as=Table;v=v1beta1;g=meta.k8s.io, application/json
I1202 03:25:40.623820   16620 round_trippers.go:393]     User-Agent: kubectl/v1.11.3 (linux/amd64) kubernetes/a452946
I1202 03:25:40.644280   16620 round_trippers.go:408] Response Status: 200 OK in 20 milliseconds
I1202 03:25:40.644308   16620 round_trippers.go:411] Response Headers:
I1202 03:25:40.644327   16620 round_trippers.go:414]     Content-Type: application/json
I1202 03:25:40.644334   16620 round_trippers.go:414]     Content-Length: 2061
I1202 03:25:40.644338   16620 round_trippers.go:414]     Date: Sun, 02 Dec 2018 03:25:40 GMT
I1202 03:25:40.644398   16620 request.go:897] Response Body: {&quot;kind&quot;:&quot;Table&quot;,&quot;apiVersion&quot;:&quot;meta.k8s.io/v1beta1&quot;,&quot;metadata&quot;:{&quot;selfLink&quot;:&quot;/api/v1/namespaces&quot;,&quot;resourceVersion&quot;:&quot;3970&quot;},&quot;columnDefinitions&quot;:[{&quot;name&quot;:&quot;Name&quot;,&quot;type&quot;:&quot;string&quot;,&quot;format&quot;:&quot;name&quot;,&quot;description&quot;:&quot;Name must be unique within anamespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names&quot;,&quot;priority&quot;:0},{&quot;name&quot;:&quot;Status&quot;,&quot;type&quot;:&quot;string&quot;,&quot;format&quot;:&quot;&quot;,&quot;description&quot;:&quot;The status of the namespace&quot;,&quot;priority&quot;:0},{&quot;name&quot;:&quot;Age&quot;,&quot;type&quot;:&quot;string&quot;,&quot;format&quot;:&quot;&quot;,&quot;description&quot;:&quot;CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.\n\nPopulated by the system. Read-only. [truncated 1037 chars]
I1202 03:25:40.645111   16620 get.go:443] no kind is registered for the type v1beta1.Table
NAME          STATUS    AGE
default       Active    45m
kube-public   Active    45m
kube-system   Active    45m
</code></pre>
<p>使用 <code>curl</code> 去请求：</p>
<pre><code>master $ curl -k  https://172.17.0.99:6443/api/v1/namespaces
{
  &quot;kind&quot;: &quot;Status&quot;,
  &quot;apiVersion&quot;: &quot;v1&quot;,
  &quot;metadata&quot;: {

  },
  &quot;status&quot;: &quot;Failure&quot;,
  &quot;message&quot;: &quot;namespaces is forbidden: User \&quot;system:anonymous\&quot; cannot list namespaces at the cluster scope&quot;,
  &quot;reason&quot;: &quot;Forbidden&quot;,
  &quot;details&quot;: {
    &quot;kind&quot;: &quot;namespaces&quot;
  },
  &quot;code&quot;: 403
}
</code></pre>
<p>看到这里，应该就很明显了，当前忽略掉认证过程的 <code>curl</code> 被判定为 <code>system:anonymous</code> 用户，而此用户不具备列出 <code>namespace</code> 的权限。</p>
<p>那我们是否有其他办法使用 <code>curl</code> 获取资源呢？ 当然有，使用 <code>kubectl proxy</code> 可以在本地和集群之间创建一个代理，就像这样：</p>
<pre><code>master $ kubectl proxy &amp;
[1] 22205
master $ Starting to serve on 127.0.0.1:8001

master $ curl http://127.0.0.1:8001/api/v1/namespaces
{
  &quot;kind&quot;: &quot;NamespaceList&quot;,
  &quot;apiVersion&quot;: &quot;v1&quot;,
  &quot;metadata&quot;: {
    &quot;selfLink&quot;: &quot;/api/v1/namespaces&quot;,
    &quot;resourceVersion&quot;: &quot;5363&quot;
  },
  &quot;items&quot;: [
    {
      &quot;metadata&quot;: {
        &quot;name&quot;: &quot;default&quot;,
        &quot;selfLink&quot;: &quot;/api/v1/namespaces/default&quot;,
        &quot;uid&quot;: &quot;a5124131-f5db-11e8-9237-0242ac110063&quot;,
        &quot;resourceVersion&quot;: &quot;4&quot;,
        &quot;creationTimestamp&quot;: &quot;2018-12-02T02:40:35Z&quot;
      },
      &quot;spec&quot;: {
        &quot;finalizers&quot;: [
          &quot;kubernetes&quot;
        ]
      },
      &quot;status&quot;: {
        &quot;phase&quot;: &quot;Active&quot;
      }
    },
    {
      &quot;metadata&quot;: {
        &quot;name&quot;: &quot;kube-public&quot;,
        &quot;selfLink&quot;: &quot;/api/v1/namespaces/kube-public&quot;,
        &quot;uid&quot;: &quot;a5153f73-f5db-11e8-9237-0242ac110063&quot;,
        &quot;resourceVersion&quot;: &quot;10&quot;,
        &quot;creationTimestamp&quot;: &quot;2018-12-02T02:40:35Z&quot;
      },
      &quot;spec&quot;: {
        &quot;finalizers&quot;: [
          &quot;kubernetes&quot;
        ]
      },
      &quot;status&quot;: {
        &quot;phase&quot;: &quot;Active&quot;
      }
    },
    {
      &quot;metadata&quot;: {
        &quot;name&quot;: &quot;kube-system&quot;,
        &quot;selfLink&quot;: &quot;/api/v1/namespaces/kube-system&quot;,
        &quot;uid&quot;: &quot;a514ad25-f5db-11e8-9237-0242ac110063&quot;,
        &quot;resourceVersion&quot;: &quot;9&quot;,
        &quot;creationTimestamp&quot;: &quot;2018-12-02T02:40:35Z&quot;
      },
      &quot;spec&quot;: {
        &quot;finalizers&quot;: [
          &quot;kubernetes&quot;
        ]
      },
      &quot;status&quot;: {
        &quot;phase&quot;: &quot;Active&quot;
      }
    }
  ]
}
</code></pre>
<p>可以看到已经能正确的获取资源了，这是因为 <code>kubectl proxy</code> 使用了 <code>$HOME/.kube/config</code> 中的配置。</p>
<p>在 <code>staging/src/k8s.io/client-go/tools/clientcmd/loader.go</code> 中，有一个名为 <code>LoadFromFile</code> 的函数用来提供加载配置文件的功能。</p>
<pre><code>func LoadFromFile(filename string) (*clientcmdapi.Config, error) {
	kubeconfigBytes, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	config, err := Load(kubeconfigBytes)
	if err != nil {
		return nil, err
	}
	glog.V(6).Infoln(&quot;Config loaded from file&quot;, filename)

	// set LocationOfOrigin on every Cluster, User, and Context
	for key, obj := range config.AuthInfos {
		obj.LocationOfOrigin = filename
		config.AuthInfos[key] = obj
	}
	for key, obj := range config.Clusters {
		obj.LocationOfOrigin = filename
		config.Clusters[key] = obj
	}
	for key, obj := range config.Contexts {
		obj.LocationOfOrigin = filename
		config.Contexts[key] = obj
	}

	if config.AuthInfos == nil {
		config.AuthInfos = map[string]*clientcmdapi.AuthInfo{}
	}
	if config.Clusters == nil {
		config.Clusters = map[string]*clientcmdapi.Cluster{}
	}
	if config.Contexts == nil {
		config.Contexts = map[string]*clientcmdapi.Context{}
	}

	return config, nil
}
</code></pre>
<p>逻辑其实很简单，读取指定的文件（一般在调用此函数前，都会先去检查是否有 <code>KUBECONFIG</code> 的环境变量或 <code>--kubeconfig</code>，如果没有才会使用默认的 <code>$HOME/.kube/config</code> 作为文件名）。</p>
<p>从以上的例子中，使用当前配置的用户可以获取资源，而 <code>system:anonymous</code> 不可以。可以得出 <code>kube-apiserver</code> 又一个重要的功能：授权。</p>
<h3>授权（Authorization）</h3>
<p>在第 8 节中，我们也已经讲过，K8S 支持多种授权机制，现在多数都在使用 <code>RBAC</code> ，我们之前使用 <code>kubeadm</code> 创建集群时，默认会开启 <code>RBAC</code>。如何创建权限可控的用户在第 8 节也已经说过。所以本节中不过多赘述了，直接看授权后的处理逻辑。</p>
<h3>准入控制（Admission Control）</h3>
<p>在请求进来时，会先经过认证、授权接下来会进入准入控制环节。准入控制和前两项内容不同，它不只是关注用户和行为，它还会处理请求的内容。不过它对读操作无效。</p>
<p>准入控制与我们前面说提到的认证、授权插件类似，支持同时开启多个。在 <code>v1.11.3</code> 中，默认开启的准入控制插件有：</p>
<pre><code>NamespaceLifecycle,LimitRanger,ServiceAccount,PersistentVolumeClaimResize,DefaultStorageClass,DefaultTolerationSeconds,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota,Priority
</code></pre>
<p>相关的代码可查看 <code>pkg/kubeapiserver/options/plugins.go</code></p>
<pre><code>func DefaultOffAdmissionPlugins() sets.String {
	defaultOnPlugins := sets.NewString(
		lifecycle.PluginName,                //NamespaceLifecycle
		limitranger.PluginName,              //LimitRanger
		serviceaccount.PluginName,           //ServiceAccount
		setdefault.PluginName,               //DefaultStorageClass
		resize.PluginName,                   //PersistentVolumeClaimResize
		defaulttolerationseconds.PluginName, //DefaultTolerationSeconds
		mutatingwebhook.PluginName,          //MutatingAdmissionWebhook
		validatingwebhook.PluginName,        //ValidatingAdmissionWebhook
		resourcequota.PluginName,            //ResourceQuota
	)

	if utilfeature.DefaultFeatureGate.Enabled(features.PodPriority) {
		defaultOnPlugins.Insert(podpriority.PluginName) //PodPriority
	}

	return sets.NewString(AllOrderedPlugins...).Difference(defaultOnPlugins)
}
</code></pre>
<p>在这里写了一些默认开启的配置。事实上，在早之前，<code>PersistentVolumeClaimResize</code> 默认是不开启的，并且开启了 <code>PersistentVolumeLabel</code>，对于移除 <code>Persistentvolumelabel</code> 感兴趣的朋友可以参考下 <a href="https://github.com/kubernetes/kubernetes/issues/52617">Remove the PersistentVolumeLabel Admission Controller</a> 。</p>
<p>这里对几个比较常见的插件做下说明：</p>
<ul>
<li>
<p>NamespaceLifecycle：它可以保证正在终止的 <code>Namespace</code> 不允许创建对象，不允许请求不存在的 <code>Namespace</code> 以及保证默认的 <code>default</code>, <code>kube-system</code> 之类的命名空间不被删除。核心的代码是：</p>
<pre><code>if a.GetOperation() == admission.Delete &amp;&amp; a.GetKind().GroupKind() == v1.SchemeGroupVersion.WithKind(&quot;Namespace&quot;).GroupKind() &amp;&amp; l.immortalNamespaces.Has(a.GetName()) {
	return errors.NewForbidden(a.GetResource().GroupResource(), a.GetName(), fmt.Errorf(&quot;this namespace may not be deleted&quot;))
}
</code></pre>
<p>如果删除默认的 <code>Namespace</code> 则会得到下面的异常：</p>
<pre><code>master $ kubectl delete ns kube-system
Error from server (Forbidden): namespaces &quot;kube-system&quot; is forbidden: this namespace may not be deleted
master $ kubectl delete ns kube-public
Error from server (Forbidden): namespaces &quot;kube-public&quot; is forbidden: this namespace may not be deleted
master $ kubectl delete ns default
Error from server (Forbidden): namespaces &quot;default&quot; is forbidden: this namespace may not be deleted
</code></pre>
</li>
<li>
<p>LimitRanger：为 <code>Pod</code> 设置默认请求资源的限制。</p>
</li>
<li>
<p>ServiceAccount：可按照预设规则创建 <code>Serviceaccount</code> 。比如都有统一的前缀：<code>system:serviceaccount:</code>。</p>
</li>
<li>
<p>DefaultStorageClass：为 <code>PVC</code> 设置默认 <code>StorageClass</code>。</p>
</li>
<li>
<p>DefaultTolerationSeconds：设置 <code>Pod</code> 的默认 forgiveness toleration 为 5 分钟。这个可能常会看到。</p>
</li>
<li>
<p>MutatingAdmissionWebhook 和 ValidatingAdmissionWebhook：这两个都是通过 Webhook 验证或者修改请求，唯一的区别是一个是顺序进行，一个是并行进行的。</p>
</li>
<li>
<p>ResourceQuota：限制 <code>Pod</code> 请求配额。</p>
</li>
<li>
<p>AlwaysPullImages：总是拉取镜像。</p>
</li>
<li>
<p>AlwaysAdmit：总是接受所有请求。</p>
</li>
</ul>
<h3>处理请求</h3>
<p>前面已经说到，一个请求依次会经过认证，授权，准入控制等环节，当这些环节都已经通过后，该请求便到了 <code>kube-apiserver</code> 的实际处理逻辑中了。</p>
<p>其实和普通的 Web server 类似，<code>kube-apiserver</code> 提供了 <code>restful</code> 的接口，增删改查等基本功能都基本类似。这里先暂时不再深入。</p>
<h2>总结</h2>
<p>通过本节，我们学习到了 <code>kube-apiserver</code> 的基本工作逻辑，各类 API 请求先后通过认证，授权，准入控制等一系列环节后，进入到 <code>kube-apiserver</code> 的 <code>Registry</code> 进行相关逻辑处理。</p>
<p>至于需要进行持久化或者需要与后端存储交互的部分，我们在下节会介绍 <code>etcd</code> 到时再看 K8S 是如何将后端存储抽象化，从 <code>etcd</code> v2 升级至 v3 的。</p>
<p><code>kube-apiserver</code> 包含的东西有很多，当你在终端下执行 <code>./kube-apiserver -h</code> 时，会发现有大量的参数。</p>
<p>这些参数除了认证，授权，准入控制相关功能外，还有审计，证书，存储等配置。主体功能、原理了解后，这些参数也就会比较容易配置了。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="11&#32;部署实践：以&#32;Helm&#32;部署项目.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="13&#32;庖丁解牛：etcd.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b4346007ff370ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
