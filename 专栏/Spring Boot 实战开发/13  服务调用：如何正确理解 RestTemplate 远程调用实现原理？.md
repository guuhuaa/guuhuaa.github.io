<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>13  服务调用：如何正确理解 RestTemplate 远程调用实现原理？.md</title>
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

                    
                    <a href="00&#32;开篇词&#32;&#32;从零开始：为什么要学习&#32;Spring&#32;Boot？.md">00 开篇词  从零开始：为什么要学习 Spring Boot？.md</a>

                </li>
                <li>

                    
                    <a href="01&#32;&#32;家族生态：如何正确理解&#32;Spring&#32;家族的技术体系？.md">01  家族生态：如何正确理解 Spring 家族的技术体系？.md</a>

                </li>
                <li>

                    
                    <a href="02&#32;&#32;案例驱动：如何剖析一个&#32;Spring&#32;Web&#32;应用程序？.md">02  案例驱动：如何剖析一个 Spring Web 应用程序？.md</a>

                </li>
                <li>

                    
                    <a href="03&#32;&#32;多维配置：如何使用&#32;Spring&#32;Boot&#32;中的配置体系？.md">03  多维配置：如何使用 Spring Boot 中的配置体系？.md</a>

                </li>
                <li>

                    
                    <a href="04&#32;&#32;定制配置：如何创建和管理自定义的配置信息？.md">04  定制配置：如何创建和管理自定义的配置信息？.md</a>

                </li>
                <li>

                    
                    <a href="05&#32;&#32;自动配置：如何正确理解&#32;Spring&#32;Boot&#32;自动配置实现原理？.md">05  自动配置：如何正确理解 Spring Boot 自动配置实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="06&#32;&#32;基础规范：如何理解&#32;JDBC&#32;关系型数据库访问规范？.md">06  基础规范：如何理解 JDBC 关系型数据库访问规范？.md</a>

                </li>
                <li>

                    
                    <a href="07&#32;&#32;数据访问：如何使用&#32;JdbcTemplate&#32;访问关系型数据库？.md">07  数据访问：如何使用 JdbcTemplate 访问关系型数据库？.md</a>

                </li>
                <li>

                    
                    <a href="08&#32;&#32;数据访问：如何剖析&#32;JdbcTemplate&#32;数据访问实现原理？.md">08  数据访问：如何剖析 JdbcTemplate 数据访问实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="09&#32;&#32;数据抽象：Spring&#32;Data&#32;如何对数据访问过程进行统一抽象？.md">09  数据抽象：Spring Data 如何对数据访问过程进行统一抽象？.md</a>

                </li>
                <li>

                    
                    <a href="10&#32;&#32;ORM&#32;集成：如何使用&#32;Spring&#32;Data&#32;JPA&#32;访问关系型数据库？.md">10  ORM 集成：如何使用 Spring Data JPA 访问关系型数据库？.md</a>

                </li>
                <li>

                    
                    <a href="11&#32;&#32;服务发布：如何构建一个&#32;RESTful&#32;风格的&#32;Web&#32;服务？.md">11  服务发布：如何构建一个 RESTful 风格的 Web 服务？.md</a>

                </li>
                <li>

                    
                    <a href="12&#32;&#32;服务调用：如何使用&#32;RestTemplate&#32;消费&#32;RESTful&#32;服务？.md">12  服务调用：如何使用 RestTemplate 消费 RESTful 服务？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="13&#32;&#32;服务调用：如何正确理解&#32;RestTemplate&#32;远程调用实现原理？.md">13  服务调用：如何正确理解 RestTemplate 远程调用实现原理？.md</a>
                    

                </li>
                <li>

                    
                    <a href="14&#32;&#32;消息驱动：如何使用&#32;KafkaTemplate&#32;集成&#32;Kafka？.md">14  消息驱动：如何使用 KafkaTemplate 集成 Kafka？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;消息驱动：如何使用&#32;JmsTemplate&#32;集成&#32;ActiveMQ？.md">15  消息驱动：如何使用 JmsTemplate 集成 ActiveMQ？.md</a>

                </li>
                <li>

                    
                    <a href="16&#32;&#32;消息驱动：如何使用&#32;RabbitTemplate&#32;集成&#32;RabbitMQ？.md">16  消息驱动：如何使用 RabbitTemplate 集成 RabbitMQ？.md</a>

                </li>
                <li>

                    
                    <a href="17&#32;&#32;安全架构：如何理解&#32;Spring&#32;安全体系的整体架构？.md">17  安全架构：如何理解 Spring 安全体系的整体架构？.md</a>

                </li>
                <li>

                    
                    <a href="18&#32;&#32;用户认证：如何基于&#32;Spring&#32;Security&#32;构建用户认证体系？.md">18  用户认证：如何基于 Spring Security 构建用户认证体系？.md</a>

                </li>
                <li>

                    
                    <a href="19&#32;&#32;服务授权：如何基于&#32;Spring&#32;Security&#32;确保请求安全访问？.md">19  服务授权：如何基于 Spring Security 确保请求安全访问？.md</a>

                </li>
                <li>

                    
                    <a href="20&#32;&#32;服务监控：如何使用&#32;Actuator&#32;组件实现系统监控？.md">20  服务监控：如何使用 Actuator 组件实现系统监控？.md</a>

                </li>
                <li>

                    
                    <a href="21&#32;&#32;指标定制：如何实现自定义度量指标和&#32;Actuator&#32;端点？.md">21  指标定制：如何实现自定义度量指标和 Actuator 端点？.md</a>

                </li>
                <li>

                    
                    <a href="22&#32;&#32;运行管理：如何使用&#32;Admin&#32;Server&#32;管理&#32;Spring&#32;应用程序？.md">22  运行管理：如何使用 Admin Server 管理 Spring 应用程序？.md</a>

                </li>
                <li>

                    
                    <a href="23&#32;&#32;数据测试：如何使用&#32;Spring&#32;测试数据访问层组件？.md">23  数据测试：如何使用 Spring 测试数据访问层组件？.md</a>

                </li>
                <li>

                    
                    <a href="24&#32;&#32;服务测试：如何使用&#32;Spring&#32;测试&#32;Web&#32;服务层组件？.md">24  服务测试：如何使用 Spring 测试 Web 服务层组件？.md</a>

                </li>
                <li>

                    
                    <a href="结束语&#32;&#32;以终为始：Spring&#32;Boot&#32;总结和展望.md">结束语  以终为始：Spring Boot 总结和展望.md</a>

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
                        <div><h1>13  服务调用：如何正确理解 RestTemplate 远程调用实现原理？</h1>
<p>在 12 讲中，我们详细描述了如何使用 RestTemplate 访问 HTTP 端点的使用方法，它涉及 RestTemplate 初始化、发起请求及获取响应结果等核心环节。今天，我们将基于上一课时中的这些环节，从源码出发让你真正理解 RestTemplate 实现远程调用的底层原理。</p>
<h3>初始化 RestTemplate 实例</h3>
<p>12 讲中我们提到可以通过 RestTemplate 提供的几个构造函数对 RestTemplate 进行初始化。在分析这些构造函数之前，我们有必要先看一下 RestTemplate 类的定义，如下代码所示：</p>
<pre><code>public class RestTemplate extends InterceptingHttpAccessor implements RestOperations
</code></pre>
<p>从上述代码中，我们可以看到 RestTemplate 扩展了 InterceptingHttpAccessor 抽象类，并实现了 RestOperations 接口。接下来我们围绕 RestTemplate 的方法定义进行设计思路的梳理。</p>
<p>首先，我们来看看 RestOperations 接口的定义，这里截取了部分核心方法，如下代码所示：</p>
<pre><code>public interface RestOperations {

 

    &lt;T&gt; T getForObject(String url, Class&lt;T&gt; responseType, Object... uriVariables) throws RestClientException;

	&lt;T&gt; ResponseEntity&lt;T&gt; getForEntity(String url, Class&lt;T&gt; responseType, Object... uriVariables) throws RestClientException;

	 

       &lt;T&gt; T postForObject(String url, @Nullable Object request, Class&lt;T&gt; responseType,Object... uriVariables) throws RestClientException;

 

	void put(String url, @Nullable Object request, Object... uriVariables) throws RestClientException;

	 

	void delete(String url, Object... uriVariables) throws RestClientException;

	&lt;T&gt; ResponseEntity&lt;T&gt; exchange(String url, HttpMethod method, @Nullable HttpEntity&lt;?&gt; requestEntity,

	 

    Class&lt;T&gt; responseType, Object... uriVariables) throws RestClientException;

	…

}
</code></pre>
<p>显然，RestOperations 接口定义了 12 讲中介绍到的 get/post/put/delete/exhange 等所有远程调用方法组，这些方法都遵循 RESTful 架构风格而设计。RestTemplate 为这些接口提供了实现机制，这是它的一条代码支线。</p>
<p>然后我们再看 InterceptingHttpAccessor，它是一个抽象类，包含的核心变量如下代码所示：</p>
<pre><code>public abstract class InterceptingHttpAccessor extends HttpAccessor {

 

    private final List&lt;ClientHttpRequestInterceptor&gt; interceptors = new ArrayList&lt;&gt;();

 

    private volatile ClientHttpRequestFactory interceptingRequestFactory;

       …

}
</code></pre>
<p>通过变量定义，我们明确了 InterceptingHttpAccessor 包含两部分处理功能，一部分负责设置和管理请求拦截器 ClientHttpRequestInterceptor，另一部分负责获取用于创建客户端 HTTP 请求的工厂类 ClientHttpRequestFactory。</p>
<p>同时，我们注意到 InterceptingHttpAccessor 同样存在一个父类 HttpAccessor，这个父类值真正实现了 ClientHttpRequestFactory 的创建及如何通过 ClientHttpRequestFactory 获取代表客户端请求的 ClientHttpRequest 对象。HttpAccessor 的核心变量如下代码所示：</p>
<pre><code>public abstract class HttpAccessor {

 

    private ClientHttpRequestFactory requestFactory = new SimpleClientHttpRequestFactory();

    …

}
</code></pre>
<p>从以上代码我们可以看到，HttpAccessor 中创建了 SimpleClientHttpRequestFactory 作为系统默认的 ClientHttpRequestFactory。关于 ClientHttpRequestFactory，我们会在本课时的后续内容中进行详细的讨论。</p>
<p>最后，针对这部分内容我们再来梳理下 RestTemplate 的类层结构，如下图所示：</p>
<p><img src="assets/Cip5yF_q_YOAHp35AAB_-PnTOp8699.png" alt="图片3.png" /></p>
<p>RestTemplate 的类层结构</p>
<p>在 RestTemplate 的类层结构中，我们能快速理解它的设计思想。整个类层结构清晰地分成两条支线，左边支线用于完成与 HTTP 请求相关的实现机制，而右边支线提供了基于 RESTful 风格的操作入口，并使用了面向对象中的接口和抽象类完成这两部分功能的聚合。</p>
<h3>RestTemplate 核心执行流程</h3>
<p>介绍完 RestTemplate 的实例化过程，接下来我们来分析它的核心执行流程。</p>
<p>作为用于远程调用的模板工具类，我们可以从具备多种请求方式的 exchange 方法入手，该方法的定义如下代码所示：</p>
<pre><code>@Override

public &lt;T&gt; ResponseEntity&lt;T&gt; exchange(String url, HttpMethod method,

            @Nullable HttpEntity&lt;?&gt; requestEntity, Class&lt;T&gt; responseType, Object... uriVariables)

            throws RestClientException {

 

        //构建请求回调

        RequestCallback requestCallback = httpEntityCallback(requestEntity, responseType);

        //构建响应体抽取器

        ResponseExtractor&lt;ResponseEntity&lt;T&gt;&gt; responseExtractor = responseEntityExtractor(responseType);

        //执行远程调用

        return nonNull(execute(url, method, requestCallback, responseExtractor, uriVariables));

}
</code></pre>
<p>显然，我们应该进一步关注这里的 execute 方法。事实上，无论我们采用 get/put/post/delete 中的哪种方法发起请求，RestTemplate 负责执行远程调用时，使用的都是 execute 方法，该方法定义如下代码所示：</p>
<pre><code>@Override

@Nullable

public &lt;T&gt; T execute(String url, HttpMethod method, @Nullable RequestCallback requestCallback, @Nullable ResponseExtractor&lt;T&gt; responseExtractor, Object... uriVariables) throws RestClientException {

 

        URI expanded = getUriTemplateHandler().expand(url, uriVariables);

        return doExecute(expanded, method, requestCallback, responseExtractor);

}
</code></pre>
<p>从以上代码中，我们发现 execute 方法首先通过 UriTemplateHandler 构建了一个 URI，然后将请求过程委托给 doExecute 方法进行处理，该方法定义如下代码所示：</p>
<pre><code>protected &lt;T&gt; T doExecute(URI url, @Nullable HttpMethod method, @Nullable RequestCallback requestCallback,

            @Nullable ResponseExtractor&lt;T&gt; responseExtractor) throws RestClientException {

 

        Assert.notNull(url, &quot;URI is required&quot;);

        Assert.notNull(method, &quot;HttpMethod is required&quot;);

        ClientHttpResponse response = null;

        try {

            //创建请求对象

            ClientHttpRequest request = createRequest(url, method);

            if (requestCallback != null) {

                //执行对请求的回调

                requestCallback.doWithRequest(request);

            }

            //获取调用结果

            response = request.execute();

            //处理调用结果

            handleResponse(url, method, response);

            //使用结果提取从结果中提取数据

            return (responseExtractor != null ? responseExtractor.extractData(response) : null);

        }

        catch (IOException ex) {

            String resource = url.toString();

            String query = url.getRawQuery();

            resource = (query != null ? resource.substring(0, resource.indexOf('?')) : resource);

            throw new ResourceAccessException(&quot;I/O error on &quot; + method.name() +

                    &quot; request for \&quot;&quot; + resource + &quot;\&quot;: &quot; + ex.getMessage(), ex);

        }

        finally {

            if (response != null) {

                response.close();

            }

        }

}
</code></pre>
<p>从上述方法中，我们发现使用 RestTemplate 进行远程调用时，主要涉及创建请求对象、执行远程调用及处理响应结果这三大步骤，下面我们分别展开说明下。</p>
<h4>创建请求对象</h4>
<p>创建请求对象的入口方法如下代码所示：</p>
<pre><code>ClientHttpRequest request = createRequest(url, method);
</code></pre>
<p>通过跟踪上面的 createRequest 方法，我们发现流程执行到了前面介绍的 HttpAccessor 类，如下代码所示：</p>
<pre><code>public abstract class HttpAccessor {

 

    private ClientHttpRequestFactory requestFactory = new SimpleClientHttpRequestFactory();

    …

 

    protected ClientHttpRequest createRequest(URI url, HttpMethod method) throws IOException {

        ClientHttpRequest request = getRequestFactory().createRequest(url, method);

        if (logger.isDebugEnabled()) {

            logger.debug(&quot;Created &quot; + method.name() + &quot; request for \&quot;&quot; + url + &quot;\&quot;&quot;);

        }

        return request;

    }

}
</code></pre>
<p>创建 ClientHttpRequest 的过程是一种典型的工厂模式应用场景，这里我们直接创建了一个实现 ClientHttpRequestFactory 接口的 SimpleClientHttpRequestFactory 对象，然后再通过这个对象的 createRequest 方法创建了客户端请求对象 ClientHttpRequest 并返回给上层组件进行使用。ClientHttpRequestFactory 接口的定义如下代码所示：</p>
<pre><code>public interface ClientHttpRequestFactory {

    //创建客户端请求对象

	ClientHttpRequest createRequest(URI uri, HttpMethod httpMethod) throws IOException;

}
</code></pre>
<p>在 Spring 中，存在一批 ClientHttpRequestFactory 接口的实现类，而SimpleClientHttpRequestFactory 是它的默认实现，在实现自定义的 ClientHttpRequestFactory 时，开发人员也可以根据需要自行选择。</p>
<p>为简单起见，我们直接跟踪 SimpleClientHttpRequestFactory 的代码，来看它的 createRequest 方法，如下代码所示：</p>
<pre><code>private boolean bufferRequestBody = true;

 

@Override

public ClientHttpRequest createRequest(URI uri, HttpMethod httpMethod) throws IOException {

        HttpURLConnection connection = openConnection(uri.toURL(), this.proxy);

        prepareConnection(connection, httpMethod.name());

 

        if (this.bufferRequestBody) {

            return new SimpleBufferingClientHttpRequest(connection, this.outputStreaming);

        }

        else {

            return new SimpleStreamingClientHttpRequest(connection, this.chunkSize, this.outputStreaming);

        }

}
</code></pre>
<p>在上述 createRequest 中，首先我们通过传入的 URI 对象构建了一个 HttpURLConnection 对象，然后对该对象进行一些预处理，最后构造并返回一个 ClientHttpRequest 实例。</p>
<p>通过翻阅代码，我们发现上述的 openConnection 方法只是通过 URL 对象的 openConnection 方法返回了一个 UrlConnection，而 prepareConnection 方法也只是完成了对 HttpUrlConnection 超时时间、请求方法等常见属性的设置。</p>
<p>在这里，我们注意到 bufferRequestBody 参数的值为 true，因此通过 createRequest 方法最终返回的结果是一个 SimpleBufferingClientHttpRequest 对象。</p>
<h4>执行远程调用</h4>
<p>一旦获取了请求对象，我们就可以发起远程调用并获取响应了，RestTemplate 中的入口方法如下代码所示：</p>
<pre><code>response = request.execute();
</code></pre>
<p>这里的 request 就是前面创建的 SimpleBufferingClientHttpRequest 类，我们可以先来看一下该类的类层结构，如下图所示：</p>
<p><img src="assets/CgpVE1_q_XeAF3WjAABzAH8vhP8188.png" alt="图片5.png" /></p>
<p>SimpleBufferingClientHttpRequest 类层结构图</p>
<p>在上图的 AbstractClientHttpRequest 中，定义了如下代码所示的 execute 方法。</p>
<pre><code>@Override

public final ClientHttpResponse execute() throws IOException {

        assertNotExecuted();

        ClientHttpResponse result = executeInternal(this.headers);

        this.executed = true;

        return result;

}

 

protected abstract ClientHttpResponse executeInternal(HttpHeaders headers) throws IOException;
</code></pre>
<p>AbstractClientHttpRequest 类的作用是防止 HTTP 请求的 Header 和 Body 被多次写入，所以在 execute 方法返回之前，我们设置了一个 executed 标志位。同时，在 execute 方法中，我们最终调用了一个抽象方法 executeInternal，这个方法的实现在 AbstractClientHttpRequest 的子类 AbstractBufferingClientHttpRequest 中，如下代码所示：</p>
<pre><code>@Override

protected ClientHttpResponse executeInternal(HttpHeaders headers) throws IOException {

        byte[] bytes = this.bufferedOutput.toByteArray();

        if (headers.getContentLength() &lt; 0) {

            headers.setContentLength(bytes.length);

        }

        ClientHttpResponse result = executeInternal(headers, bytes);

        this.bufferedOutput = new ByteArrayOutputStream(0);

        return result;

}

 

protected abstract ClientHttpResponse executeInternal(HttpHeaders headers, byte[] bufferedOutput)    throws IOException;
</code></pre>
<p>和 AbstractClientHttpRequest 类一样，我们进一步梳理了一个抽象方法 executeInternal，这个抽象方法通过最底层的 SimpleBufferingClientHttpRequest 类实现，如下代码所示：</p>
<pre><code>@Override

protected ClientHttpResponse executeInternal(HttpHeaders headers, byte[] bufferedOutput) throws IOException {

        addHeaders(this.connection, headers);

        // JDK &lt;1.8 doesn't support getOutputStream with HTTP DELETE

        if (getMethod() == HttpMethod.DELETE &amp;&amp; bufferedOutput.length == 0) {

            this.connection.setDoOutput(false);

        }

        if (this.connection.getDoOutput() &amp;&amp; this.outputStreaming) {

            this.connection.setFixedLengthStreamingMode(bufferedOutput.length);

        }

        this.connection.connect();

        if (this.connection.getDoOutput()) {

            FileCopyUtils.copy(bufferedOutput, this.connection.getOutputStream());

        }

        else {

            // Immediately trigger the request in a no-output scenario as well

            this.connection.getResponseCode();

        }

        return new SimpleClientHttpResponse(this.connection);

}
</code></pre>
<p>这里通过 FileCopyUtils.copy 工具方法，我们把结果写入输出流上了，executeInternal 方法最终返回的结果是一个包装了 Connection 对象的 SimpleClientHttpResponse。</p>
<h4>处理响应结果</h4>
<p>一个 HTTP 请求处理的最后一步是从 ClientHttpResponse 中读取输入流，然后格式化为一个响应体并将其转化为业务对象，入口代码如下所示：</p>
<pre><code>//处理调用结果

handleResponse(url, method, response);

//使用结果提取从结果中提取数据

return (responseExtractor != null ? responseExtractor.extractData(response) : null);
</code></pre>
<p>我们先来看这里的 handleResponse 方法，定义如下代码所示：</p>
<pre><code>protected void handleResponse(URI url, HttpMethod method, ClientHttpResponse response) throws IOException {

        ResponseErrorHandler errorHandler = getErrorHandler();

        boolean hasError = errorHandler.hasError(response);

        if (logger.isDebugEnabled()) {

            try {

                logger.debug(method.name() + &quot; request for \&quot;&quot; + url + &quot;\&quot; resulted in &quot; +

                        response.getRawStatusCode() + &quot; (&quot; + response.getStatusText() + &quot;)&quot; +

                        (hasError ? &quot;; invoking error handler&quot; : &quot;&quot;));

            }

            catch (IOException ex) {

                // ignore

            }

        }

        if (hasError) {

            errorHandler.handleError(url, method, response);

        }

}
</code></pre>
<p>以上代码中，通过 getErrorHandler 方法我们获取了一个 ResponseErrorHandler，如果响应的状态码错误，我们可以调用 handleError 来处理错误并抛出异常。在这里，我们发现这段代码实际上并没有真正处理返回的数据，而只是执行了错误处理。</p>
<p>而获取响应数据并完成转化的工作是在 ResponseExtractor 中，该接口定义如下代码所示：</p>
<pre><code>public interface ResponseExtractor&lt;T&gt; {

 

    @Nullable

    T extractData(ClientHttpResponse response) throws IOException;

}
</code></pre>
<p>在 RestTemplate 类中，我们定义了一个 ResponseEntityResponseExtractor 内部类实现了ResponseExtractor 接口，如下代码所示：</p>
<pre><code>private class ResponseEntityResponseExtractor &lt;T&gt; implements ResponseExtractor&lt;ResponseEntity&lt;T&gt;&gt; {

 

        @Nullable

        private final HttpMessageConverterExtractor&lt;T&gt; delegate;

 

        public ResponseEntityResponseExtractor(@Nullable Type responseType) {

            if (responseType != null &amp;&amp; Void.class != responseType) {

                this.delegate = new HttpMessageConverterExtractor&lt;&gt;(responseType, getMessageConverters(), logger);

            }

            else {

                this.delegate = null;

            }

        }

 

        @Override

        public ResponseEntity&lt;T&gt; extractData(ClientHttpResponse response) throws IOException {

            if (this.delegate != null) {

                T body = this.delegate.extractData(response);

                return ResponseEntity.status(response.getRawStatusCode()).headers(response.getHeaders()).body(body);

            }

            else {

                return ResponseEntity.status(response.getRawStatusCode()).headers(response.getHeaders()).build();

            }

        }

}
</code></pre>
<p>在上述代码中，ResponseEntityResponseExtractor 中的 extractData 方法本质上是将数据提取部分的工作委托给了一个代理对象 delegate，而这个 delegate 的类型就是 HttpMessageConverterExtractor。</p>
<p>从命名上看，我们不难看出 HttpMessageConverterExtractor 类的内部使用了 12 讲介绍的 HttpMessageConverter 实现消息的转换，如下代码所示（代码做了裁剪）：</p>
<pre><code>public class HttpMessageConverterExtractor&lt;T&gt; implements ResponseExtractor&lt;T&gt; {

 

    private final List&lt;HttpMessageConverter&lt;?&gt;&gt; messageConverters;

 

@Override

    @SuppressWarnings({&quot;unchecked&quot;, &quot;rawtypes&quot;, &quot;resource&quot;})

    public T extractData(ClientHttpResponse response) throws IOException {

        MessageBodyClientHttpResponseWrapper responseWrapper = new MessageBodyClientHttpResponseWrapper(response);

        if (!responseWrapper.hasMessageBody() || responseWrapper.hasEmptyMessageBody()) {

            return null;

        }

        MediaType contentType = getContentType(responseWrapper);

 

        try {

            for (HttpMessageConverter&lt;?&gt; messageConverter : this.messageConverters) {

                if (messageConverter instanceof GenericHttpMessageConverter) {

                    GenericHttpMessageConverter&lt;?&gt; genericMessageConverter =

                            (GenericHttpMessageConverter&lt;?&gt;) messageConverter;

                    if (genericMessageConverter.canRead(this.responseType, null, contentType)) {

                        return (T) genericMessageConverter.read(this.responseType, null, responseWrapper);

                    }

                }

                if (this.responseClass != null) {

                    if (messageConverter.canRead(this.responseClass, contentType)) {

                        return (T) messageConverter.read((Class) this.responseClass, responseWrapper);

                    }

                }

            }

        }

	…

}
</code></pre>
<p>上述方法看上去有点复杂，但核心逻辑很简单，首先遍历 HttpMessageConveter 列表，然后判断其是否能够读取数据，如果能就调用 read 方法读取数据。</p>
<p>最后，我们讨论下 HttpMessageConveter 中如何实现 read 方法。</p>
<p>先来看 HttpMessageConveter 接口的抽象实现类 AbstractHttpMessageConverter，在它的 read 方法中我们同样定义了一个抽象方法 readInternal，如下代码所示：</p>
<pre><code>@Override

public final T read(Class&lt;? extends T&gt; clazz, HttpInputMessage inputMessage)            throws IOException, HttpMessageNotReadableException {

 

    return readInternal(clazz, inputMessage);

}

 

protected abstract T readInternal(Class&lt;? extends T&gt; clazz, HttpInputMessage inputMessage) throws IOException, HttpMessageNotReadableException;
</code></pre>
<p>在 12 讲中，我们提到 Spring 提供了一系列的 HttpMessageConveter 实现消息的转换，而最简单的实现方式是 StringHttpMessageConverter，该类的 read 方法如下代码所示：</p>
<pre><code>@Override

protected String readInternal(Class&lt;? extends String&gt; clazz, HttpInputMessage inputMessage) throws IOException {

    Charset charset = getContentTypeCharset(inputMessage.getHeaders().getContentType());

    return StreamUtils.copyToString(inputMessage.getBody(), charset);

}
</code></pre>
<p>StringHttpMessageConverter 的实现过程：首先从输入消息 HttpInputMessage 中通过 getBody 方法获取消息体，也就是一个 ClientHttpResponse 对象，再通过 copyToString 方法从该对象中读取数据，并返回字符串结果。</p>
<p>至此，通过 RestTemplate 发起、执行及响应整个 HTTP 请求的完整流程就介绍完毕了。</p>
<h3>从源码解析到日常开发</h3>
<p>本节课涉及了大量关于如果处理 HTTP 请求的实现细节，而这些实现细节对开发人员理解 HTTP 协议、掌握 HTTP 协议及远程调用很大帮助，后期，你可以根据实际需要针对某些细节进一步深入分析。</p>
<p>同时，通过对 RestTemplate 本身及围绕它的多个工具类的设计和实现过程进行梳理，也可以加深我们对抽象类与接口的标准设计理念的理解，并将这些设计理念付诸日常开发过程中。</p>
<h3>小结与预告</h3>
<p>我们要想深入理解和掌握一个 HTTP 请求的处理过程，剖析 RestTemplate 工具类的实现很有必要。</p>
<p>RestTemplate 中提供了创建请求对象、执行远程调用及处理响应结果这三大步骤的完整实现思路。本节课中我们对这些步骤进行了详细说明，并分析了其中包含的设计理念及实现技巧。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="12&#32;&#32;服务调用：如何使用&#32;RestTemplate&#32;消费&#32;RESTful&#32;服务？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="14&#32;&#32;消息驱动：如何使用&#32;KafkaTemplate&#32;集成&#32;Kafka？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d27cdf970ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
            document.getElementById("tip").innerHTML = "<a href='https://learn.lianglianglee.com/%E4%B8%93%E6%A0%8F/Spring%20Boot%20%E5%AE%9E%E6%88%98%E5%BC%80%E5%8F%91/&quot;&#32;+&#32;cookie&#32;+&#32;&quot;'>跳转到上次进度</a>"
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
