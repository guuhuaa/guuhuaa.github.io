<!DOCTYPE html>
<!-- saved from url=(0046)https://kaiiiz.github.io/hexo-theme-book-demo/ -->
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
        <link rel="icon" href="../../static/favicon.png">
        <title>16  消息驱动：如何使用 RabbitTemplate 集成 RabbitMQ？.md</title>
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

                    
                    <a href="13&#32;&#32;服务调用：如何正确理解&#32;RestTemplate&#32;远程调用实现原理？.md">13  服务调用：如何正确理解 RestTemplate 远程调用实现原理？.md</a>

                </li>
                <li>

                    
                    <a href="14&#32;&#32;消息驱动：如何使用&#32;KafkaTemplate&#32;集成&#32;Kafka？.md">14  消息驱动：如何使用 KafkaTemplate 集成 Kafka？.md</a>

                </li>
                <li>

                    
                    <a href="15&#32;&#32;消息驱动：如何使用&#32;JmsTemplate&#32;集成&#32;ActiveMQ？.md">15  消息驱动：如何使用 JmsTemplate 集成 ActiveMQ？.md</a>

                </li>
                <li>

                    <a class="current-tab" href="16&#32;&#32;消息驱动：如何使用&#32;RabbitTemplate&#32;集成&#32;RabbitMQ？.md">16  消息驱动：如何使用 RabbitTemplate 集成 RabbitMQ？.md</a>
                    

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
                        <div><h1>16  消息驱动：如何使用 RabbitTemplate 集成 RabbitMQ？</h1>
<p>15 讲我们介绍了基于 ActiveMQ 和 JmsTemplate 实现消息发送和消费，并重构了 SpringCSS 案例系统中的 account-service 和 customer-service 服务。</p>
<p>今天，我们将介绍另一款主流的消息中间件 RabbitMQ，并基于 RabbitTemplate 模板工具类为 SpringCSS 案例添加对应的消息通信机制。</p>
<h3>AMQP 规范与 RabbitMQ</h3>
<p>AMQP（Advanced Message Queuing Protocol）是一个提供统一消息服务的应用层标准高级消息队列规范。和 JMS 规范一样，AMQP 描述了一套模块化的组件及组件之间进行连接的标准规则，用于明确客户端与服务器交互的语义。而业界也存在一批实现 AMQP 规范的框架，其中极具代表性的是 RabbitMQ。</p>
<h4>AMQP 规范</h4>
<p>在 AMQP 规范中存在三个核心组件，分别是交换器（Exchange）、消息队列（Queue）和绑定（Binding）。其中交换器用于接收应用程序发送的消息，并根据一定的规则将这些消息路由发送到消息队列中；消息队列用于存储消息，直到这些消息被消费者安全处理完毕；而绑定定义了交换器和消息队列之间的关联，为它们提供了路由规则。</p>
<p>在 AMQP 规范中并没有明确指明类似 JMS 中一对一的点对点模型和一对多的发布-订阅模型，不过通过控制 Exchange 与 Queue 之间的路由规则，我们可以很容易地模拟 Topic 这种典型消息中间件的概念。</p>
<p>如果存在多个 Queue，Exchange 如何知道把消息发送到哪个 Queue 中呢？</p>
<p>通过 Binding 规则设置路由信息即可。在与多个 Queue 关联之后，Exchange 中会存在一个路由表，这个表中维护着每个 Queue 存储消息的限制条件。</p>
<p>消息中包含一个路由键（Routing Key），它由消息发送者产生，并提供给 Exchange 路由这条消息的标准。而 Exchange 会检查 Routing Key，并结合路由算法决定将消息路由发送到哪个 Queue 中。</p>
<p>通过下面 Exchange 与 Queue 之间的路由关系图，我们可以看到一条来自生产者的消息通过 Exchange 中的路由算法可以发送给一个或多个 Queue，从而实现点对点和发布订阅功能。</p>
<p><img src="assets/CgqCHl_4DTKAbAiPAADqglSjwTc554.png" alt="图片7.png" /></p>
<p>AMQP 路由关系图</p>
<p>上图中，不同的路由算法存在不同的 Exchange 类型，而 AMQP 规范中指定了直接式交换器（Direct Exchange）、广播式交换器（Fanout Exchange）、主题式交换器（Topic Exchange）和消息头式交换器（Header Exchange）这几种 Exchange 类型，不过这一讲我们将重点介绍直接式交换器。</p>
<p>通过精确匹配消息的 Routing Key，直接式交换器可以将消息路由发送到零个或多个队列中，如下图所示：</p>
<p><img src="assets/Ciqc1F_4DTqAJ5kHAADKl5uWm0U797.png" alt="图片8.png" /></p>
<p>Direct Exchange 示意图</p>
<h4>RabbitMQ 基本架构</h4>
<p>RabbitMQ 使用 Erlang 语言开发的 AMQP 规范标准实现框架，而 ConnectionFactory、Connection、Channel 是 RabbitMQ 对外提供的 API 中最基本的对象，都需要遵循 AMQP 规范的建议。其中，Channel 是应用程序与 RabbitMQ 交互过程中最重要的一个接口，因为我们大部分的业务操作需要通过 Channel 接口完成，如定义 Queue、定义 Exchange、绑定 Queue 与 Exchange、发布消息等。</p>
<p>如果想启动 RabbitMQ，我们只需要运行 rabbitmq-server.sh 文件即可。不过，因为 RabbitMQ 依赖于 Erlang，所以首先我们需要确保安装上 Erlang 环境。</p>
<p>接下来，我们一起看下如何使用 Spring 框架所提供的 RabbitTemplate 模板工具类集成 RabbitMQ。</p>
<h3>使用 RabbitTemplate 集成 RabbitMQ</h3>
<p>如果想使用 RabbitTemplate 集成 RabbitMQ，首先我们需要在 Spring Boot 应用程序中添加对 spring-boot-starter-amqp 的依赖，如下代码所示：</p>
<pre><code>&lt;dependency&gt;

    &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;

    &lt;artifactId&gt;spring-boot-starter-amqp&lt;/artifactId&gt;

&lt;/dependency&gt;
</code></pre>
<h4>使用 RabbitTemplate 发送消息</h4>
<p>和其他模板类一样，RabbitTemplate 也提供了一批 send 方法用来发送消息，如下代码所示：</p>
<pre><code>@Override

public void send(Message message) throws AmqpException {

    send(this.exchange, this.routingKey, message);

}

 

@Override

public void send(String routingKey, Message message) throws AmqpException {

    send(this.exchange, routingKey, message);

}

 

@Override

public void send(final String exchange, final String routingKey, final Message message) throws AmqpException {

    send(exchange, routingKey, message, null);

}
</code></pre>
<p>在这里可以看到，我们指定了消息发送的 Exchange 及用于消息路由的路由键 RoutingKey。因为这些 send 方法发送的是原生消息对象，所以在与业务代码进行集成时，我们需要将业务对象转换为 Message 对象，示例代码如下所示：</p>
<pre><code>public void sendDemoObject(DemoObject demoObject) { 

    MessageConverter converter =               rabbitTemplate.getMessageConverter(); 

    MessageProperties props = new MessageProperties(); 

    Message message = converter.toMessage(demoObject, props); 

    rabbitTemplate.send(&quot;demo.queue&quot;, message); 

}
</code></pre>
<p>如果我们不想在业务代码中嵌入 Message 等原生消息对象，还可以使用 RabbitTemplate 的 convertAndSend 方法组进行实现，如下代码所示：</p>
<pre><code>@Override

public void convertAndSend(Object object) throws AmqpException {

        convertAndSend(this.exchange, this.routingKey, object, (CorrelationData) null);

}

 

@Override

public void correlationConvertAndSend(Object object, CorrelationData correlationData) throws AmqpException {

        convertAndSend(this.exchange, this.routingKey, object, correlationData);

}

 

@Override

public void convertAndSend(String routingKey, final Object object) throws AmqpException {

        convertAndSend(this.exchange, routingKey, object, (CorrelationData) null);

}

 

@Override

public void convertAndSend(String routingKey, final Object object, CorrelationData correlationData)

            throws AmqpException {

        convertAndSend(this.exchange, routingKey, object, correlationData);

}

 

@Override

public void convertAndSend(String exchange, String routingKey, final Object object) throws AmqpException {

        convertAndSend(exchange, routingKey, object, (CorrelationData) null);

}
</code></pre>
<p>上述 convertAndSend 方法组在内部就完成了业务对象向原生消息对象的自动转换过程，因此，我们可以使用如下所示的代码来简化消息发送过程。</p>
<pre><code>public void sendDemoObject(DemoObject demoObject) { 

	rabbitTemplate.convertAndSend(&quot;demo.queue&quot;, demoObject); 

}
</code></pre>
<p>当然，有时候我们需要在消息发送的过程中为消息添加一些属性，这就不可避免需要操作原生 Message 对象，而 RabbitTemplate 也提供了一组 convertAndSend 重载方法应对这种场景，如下代码所示：</p>
<pre><code>@Override

public void convertAndSend(String exchange, String routingKey, final Object message,

            final MessagePostProcessor messagePostProcessor, CorrelationData correlationData) throws AmqpException {

        Message messageToSend = convertMessageIfNecessary(message);

        messageToSend = messagePostProcessor.postProcessMessage(messageToSend, correlationData);

        send(exchange, routingKey, messageToSend, correlationData);

}
</code></pre>
<p>注意这里，我们使用了一个 MessagePostProcessor 类对所生成的消息进行后处理，MessagePostProcessor 的使用方式如下代码所示：</p>
<pre><code>rabbitTemplate.convertAndSend(“demo.queue”, event, new MessagePostProcessor() {

     @Override

     public Message postProcessMessage(Message message) throws AmqpException {

          //针对 Message 的处理

          return message;

     }

});
</code></pre>
<p>使用 RabbitTemplate 的最后一步是在配置文件中添加配置项，在配置时我们需要指定 RabbitMQ 服务器的地址、端口、用户名和密码等信息，如下代码所示：</p>
<pre><code>spring:

  rabbitmq:

    host: 127.0.0.1

    port: 5672

    username: guest

    password: guest

    virtual-host: DemoHost
</code></pre>
<p><strong>注意，出于对多租户和安全因素的考虑，AMQP 还提出了虚拟主机（Virtual Host）概念，因此这里出现了一个 virtual-host 配置项。</strong></p>
<p>Virtual Host 类似于权限控制组，内部可以包含若干个 Exchange 和 Queue。多个不同用户使用同一个 RabbitMQ 服务器提供的服务时，我们可以将其划分为多个 Virtual Host，并在自己的 Virtual Host 中创建相应组件，如下图所示：</p>
<p><img src="assets/CgqCHl_4DUiAGJuEAAC1QELaeNI351.png" alt="图片9.png" /></p>
<p>添加了 Virtual Host 的 AMQP 模型</p>
<h4>使用 RabbitTemplate 消费消息</h4>
<p>和 JmsTemplate 一样，使用 RabbitTemplate 消费消息时，我们也可以使用推模式和拉模式。</p>
<p>在拉模式下，使用 RabbitTemplate 的典型示例如下代码所示：</p>
<pre><code>public DemoEvent receiveEvent() {

        return (DemoEvent) rabbitTemplate.receiveAndConvert(“demo.queue”);

}
</code></pre>
<p>这里，我们使用了 RabbitTemplate 中的 receiveAndConvert 方法，该方法可以从一个指定的 Queue 中拉取消息，如下代码所示：</p>
<pre><code>@Override

public Object receiveAndConvert(String queueName) throws AmqpException {

        return receiveAndConvert(queueName, this.receiveTimeout);

}
</code></pre>
<p>这里请注意，内部的 receiveAndConvert 方法中出现了第二个参数 receiveTimeout，这个参数的默认值是 0，意味着即使调用 receiveAndConvert 时队列中没有消息，该方法也会立即返回一个空对象，而不会等待下一个消息的到来，这点与 15 讲介绍的 JmsTemplate 存在本质性的区别。</p>
<p>如果我们想实现与 JmsTemplate 一样的阻塞等待，设置好 receiveTimeout 参数即可，如下代码所示：</p>
<pre><code>public DemoEvent receiveEvent() { 

	return (DemoEvent)rabbitTemplate.receiveAndConvert(&quot;demo.queue&quot;, 2000ms); 

}
</code></pre>
<p>如果不想每次方法调用都指定 receiveTimeout，我们可以在配置文件中通过添加配置项的方式设置 RabbitTemplate 级别的时间，如下代码所示：</p>
<pre><code>spring:

  rabbitmq:

    template:

      receive-timeout: 2000
</code></pre>
<p>当然，RabbitTemplate 也提供了一组支持接收原生消息的 receive 方法，但我们还是建议使用 receiveAndConvert 方法实现拉模式下的消息消费。</p>
<p>介绍完拉模式，接下来我们介绍推模式，它的实现方法也很简单，如下代码所示：</p>
<pre><code>@RabbitListener(queues = “demo.queue”)

public void handlerEvent(DemoEvent event) {

    //TODO：添加消息处理逻辑

}
</code></pre>
<p>开发人员在 @RabbitListener 中指定目标队列即可自动接收来自该队列的消息，这种实现方式与 15 讲中介绍的 @JmsListener 完全一致。</p>
<h3>在 SpringCSS 案例中集成 RabbitMQ</h3>
<p>因为这三种模板工具类的使用方式非常类似，都可以用来提取公共代码形成统一的接口和抽象类，所以作为介绍消息中间件的最后一讲，我们想对 SpringCSS 案例中的三种模板工具类的集成方式进行抽象。</p>
<h4>实现 account-service 消息生产者</h4>
<p>在消息生产者的 account-service 中，我们提取了如下所示的 AccountChangedPublisher 作为消息发布的统一接口。</p>
<pre><code>public interface AccountChangedPublisher {

    void publishAccountChangedEvent(Account account, String operation);

}
</code></pre>
<p>请注意，这是一个面向业务的接口，没有使用用于消息通信的 AccountChangedEvent 对象。</p>
<p>而我们将在 AccountChangedPublisher 接口的实现类 AbstractAccountChangedPublisher 中完成对 AccountChangedEvent 对象的构建，如下代码所示：</p>
<pre><code>public abstract class AbstractAccountChangedPublisher implements AccountChangedPublisher {

 

    @Override

    public void publishAccountChangedEvent(Account account, String operation) {

 

        AccountMessage accountMessage = new AccountMessage(account.getId(), account.getAccountCode(), account.getAccountName());

        AccountChangedEvent event = new AccountChangedEvent(AccountChangedEvent.class.getTypeName(),

                operation.toString(), accountMessage);

 

        publishEvent(event);

    }

 

    protected abstract void publishEvent(AccountChangedEvent event);

}
</code></pre>
<p>AbstractAccountChangedPublisher 是一个抽象类，我们基于传入的业务对象构建了一个消息对象 AccountChangedEvent，并通过 publishEvent 抽象方法发送消息。</p>
<p>针对不同的消息中间件，我们需要分别实现对应的 publishEvent 方法。以 Kafka 为例，我们重构了原有代码并提供了如下所示的 KafkaAccountChangedPublisher 实现类。</p>
<pre><code>@Component(&quot;kafkaAccountChangedPublisher&quot;)

public class KafkaAccountChangedPublisher extends AbstractAccountChangedPublisher {

 

    @Autowired

    private KafkaTemplate&lt;String, AccountChangedEvent&gt; kafkaTemplate;

    @Override

    protected void publishEvent(AccountChangedEvent event) {

        kafkaTemplate.send(AccountChannels.SPRINGCSS_ACCOUNT_TOPIC, event);

    }

}
</code></pre>
<p>对 RabbitMQ 而言，RabbitMQAccountChangedPublisher 的实现方式也是类似，如下代码所示：</p>
<pre><code>@Component(&quot;rabbitMQAccountChangedPublisher&quot;)

public class RabbitMQAccountChangedPublisher extends AbstractAccountChangedPublisher {

 

    @Autowired

    private RabbitTemplate rabbitTemplate;

    @Override

    protected void publishEvent(AccountChangedEvent event) {

        rabbitTemplate.convertAndSend(AccountChannels.SPRINGCSS_ACCOUNT_QUEUE, event, new MessagePostProcessor() {

            @Override

            public Message postProcessMessage(Message message) throws AmqpException {

                MessageProperties props = message.getMessageProperties();

                props.setHeader(&quot;EVENT_SYSTEM&quot;, &quot;SpringCSS&quot;);

                return message;

            }

        });

    }

}
</code></pre>
<p>对于 RabbitMQ 而言，在使用 RabbitMQAccountChangedPublisher 发送消息之前，我们需要先初始化 Exchange、Queue，以及两者之间的 Binding 关系，因此我们实现了如下所示的 RabbitMQMessagingConfig 配置类。</p>
<pre><code>@Configuration

public class RabbitMQMessagingConfig {

 

    public static final String SPRINGCSS_ACCOUNT_DIRECT_EXCHANGE = &quot;springcss.account.exchange&quot;;

    public static final String SPRINGCSS_ACCOUNT_ROUTING = &quot;springcss.account.routing&quot;;

 

    @Bean

    public Queue SpringCssDirectQueue() {

        return new Queue(AccountChannels.SPRINGCSS_ACCOUNT_QUEUE, true);

    }

 

    @Bean

    public DirectExchange SpringCssDirectExchange() {

        return new DirectExchange(SPRINGCSS_ACCOUNT_DIRECT_EXCHANGE, true, false);

    }

 

    @Bean

    public Binding bindingDirect() {

        return BindingBuilder.bind(SpringCssDirectQueue()).to(SpringCssDirectExchange())

                .with(SPRINGCSS_ACCOUNT_ROUTING);

    }

 

    @Bean

    public Jackson2JsonMessageConverter rabbitMQMessageConverter() {

        return new Jackson2JsonMessageConverter();

    }

}
</code></pre>
<p>上述代码中初始化了一个 DirectExchange、一个 Queue ，并设置了两者之间的绑定关系，同时我们还初始化了一个 Jackson2JsonMessageConverter 用于在消息发送过程中将消息转化为序列化对象，以便在网络上进行传输。</p>
<h4>实现 customer-service 消息消费者</h4>
<p>现在，回到 customer-service 服务，我们先看看提取用于接收消息的统一化接口 AccountChangedReceiver，如下代码所示：</p>
<pre><code>public interface AccountChangedReceiver {

    //Pull 模式下的消息接收方法

    void receiveAccountChangedEvent();

    //Push 模式下的消息接收方法

    void handlerAccountChangedEvent(AccountChangedEvent event);

}
</code></pre>
<p>AccountChangedReceiver 分别定义了拉取模式和推送模式下的消息接收方法，同样我们也提取了一个抽象实现类 AbstractAccountChangedReceiver，如下代码所示：</p>
<pre><code>public abstract class AbstractAccountChangedReceiver implements AccountChangedReceiver {

 

    @Autowired

    LocalAccountRepository localAccountRepository;

 

    @Override

    public void receiveAccountChangedEvent() {

 

        AccountChangedEvent event = receiveEvent();

 

        handleEvent(event);

    }

 

    protected void handleEvent(AccountChangedEvent event) {

        AccountMessage account = event.getAccountMessage();

        String operation = event.getOperation();

 

        operateAccount(account, operation);

    }

 

    private void operateAccount(AccountMessage accountMessage, String operation) {

        System.out.print(

                accountMessage.getId() + &quot;:&quot; + accountMessage.getAccountCode() + &quot;:&quot; + accountMessage.getAccountName());

 

        LocalAccount localAccount = new LocalAccount(accountMessage.getId(), accountMessage.getAccountCode(),

                accountMessage.getAccountName());

 

        if (operation.equals(&quot;ADD&quot;) || operation.equals(&quot;UPDATE&quot;)) {

            localAccountRepository.save(localAccount);

        } else {

            localAccountRepository.delete(localAccount);

        }

    }

 

    protected abstract AccountChangedEvent receiveEvent();

}
</code></pre>
<p>这里实现了 AccountChangedReceiver 接口的 receiveAccountChangedEvent 方法，并定义了一个 receiveEvent 抽象方法接收来自不同消息中间件的 AccountChangedEvent 消息。一旦 receiveAccountChangedEvent 方法获取了消息，我们将根据其中的 Account 对象及对应的操作更新本地数据库。</p>
<p>接下来我们看看 AbstractAccountChangedReceiver 中的一个实现类 RabbitMQAccountChangedReceiver，如下代码所示：</p>
<pre><code>@Component(&quot;rabbitMQAccountChangedReceiver&quot;)

public class RabbitMQAccountChangedReceiver extends AbstractAccountChangedReceiver {

 

    @Autowired

    private RabbitTemplate rabbitTemplate;

 

    @Override

    public AccountChangedEvent receiveEvent() {

        return (AccountChangedEvent) rabbitTemplate.receiveAndConvert(AccountChannels.SPRINGCSS_ACCOUNT_QUEUE);

    }

 

    @Override

    @RabbitListener(queues = AccountChannels.SPRINGCSS_ACCOUNT_QUEUE)

    public void handlerAccountChangedEvent(AccountChangedEvent event) {

        super.handleEvent(event);

    }

}
</code></pre>
<p>上述 RabbitMQAccountChangedReceiver 同时实现了 AbstractAccountChangedReceiver 的 receiveEvent 抽象方法及 AccountChangedReceiver 接口中的 handlerAccountChangedEvent 方法。其中 receiveEvent 方法用于主动拉取消息，而 handlerAccountChangedEvent 方法用于接受推动过来的消息，在该方法上我们添加了 @RabbitListener 注解。</p>
<p>接着我们来看下同样继承了 AbstractAccountChangedReceiver 抽象类的 KafkaAccountChangedListener 类，如下代码所示：</p>
<pre><code>@Component

public class KafkaAccountChangedListener extends AbstractAccountChangedReceiver {

 

    @Override

    @KafkaListener(topics = AccountChannels.SPRINGCSS_ACCOUNT_TOPIC)

    public void handlerAccountChangedEvent(AccountChangedEvent event) {

 

        super.handleEvent(event);

    }

 

    @Override

    protected AccountChangedEvent receiveEvent() {

        return null;

    }

}
</code></pre>
<p>我们知道 Kafka 只能通过推送方式获取消息，所以它只实现了 handlerAccountChangedEvent 方法，而 receiveEvent 方法为空。</p>
<h3>小结与预告</h3>
<p>这一讲，我们学习了最后一款消息中间件 RabbitMQ，并使用 Spring Boot 提供的 RabbitTemplate 完成了消息的发送和消费。同时，基于三种消息中间件的对接方式，我们提取了它们之间的共同点，并抽取了对应的接口和抽象类，重构了 SpringCSS 系统的实现过程。</p>
<p>Spring 为我们提供了一整套完整的安全解决方案，17 讲我们将对这套解决方案展开讨论。</p>
</div>
                    </div>
                    <div>
                        <div style="float: left">
                            <a href="15&#32;&#32;消息驱动：如何使用&#32;JmsTemplate&#32;集成&#32;ActiveMQ？.md">上一页</a>
                        </div>
                        <div style="float: right">
                            <a href="17&#32;&#32;安全架构：如何理解&#32;Spring&#32;安全体系的整体架构？.md">下一页</a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>

    <a class="off-canvas-overlay" onclick="hide_canvas()"></a>
</div>
<script defer src="https://static.cloudflareinsights.com/beacon.min.js/v64f9daad31f64f81be21cbef6184a5e31634941392597" integrity="sha512-gV/bogrUTVP2N3IzTDKzgP0Js1gg4fbwtYB6ftgLbKQu/V8yH2+lrKCfKHelh4SO3DPzKj4/glTO+tNJGDnb0A==" data-cf-beacon='{"rayId":"6b434d38a83270ac","version":"2021.11.0","r":1,"token":"1f5d475227ce4f0089a7cff1ab17c0f5","si":100}' crossorigin="anonymous"></script>
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
