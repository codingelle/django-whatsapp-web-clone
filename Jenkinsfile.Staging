pipeline {
  agent { label "sweetheart" }
  environment {
    MYHOME = "$HOME/Documents/django-whatsapp-web-clone"
  }
  stages {
    stage("Build") {
      steps {
        // 63791,54321 to avoid clash w. prod port
        sh """
            git clone https://github.com/codingelle/django-whatsapp-web-clone.git
            podman pod create -n staging-pod -p 63791:6379 -p 54321:5432
            podman run --pod=staging-pod -d --name redis-staging-svc registry.redhat.io/rhel8/redis-5:1-160.1647451816
            podman run --pod=staging-pod -d --name psql-staging-svc --env-file=$MYHOME/.env.staging registry.redhat.io/rhel8/postgresql-12:1-99.1647451835
        """
        //podman run --pod=staging-pod -d --name app-svc --env-file=$MYHOME/.env.staging localhost/django-app:latest
      }
    }

    stage("Test") {
      steps {
        sh 'podman run -u root --pod staging-pod --name app-staging-svc --env-file=$MYHOME/.env.staging -v $MYHOME/:/opt/app-root/src/ registry.access.redhat.com/ubi8/python-38 bash -c "pip install -U pip && pip install -r requirements.txt && python manage.py migrate && python manage.py createsuperuser --no-input && python manage.py test"'
        //sh 'podman run -u root --pod staging-pod --name app-svc --env-file=$MYHOME/.env.staging -v $MYHOME/:/opt/app-root/src/ registry.access.redhat.com/ubi8/python-38 bash -c "pip install -U pip && pip install -r requirements.txt && python manage.py migrate && python manage.py createsuperuser --no-input && daphne -b 0.0.0.0 -p 8080 django_channel_tutorial.asgi:application && python manage.py test"'
      }
    }

    stage("Deploy") {
      steps {
        echo "Deploy here"
        dir("$MYHOME") {
            //sh "git pull origin master"
            git credentialsId: 'GithubPassphrase', url: 'https://github.com/codingelle/django-whatsapp-web-clone'
            // restart all services?
        }
      }
    }
  }
  post {
    // Clean after build
    always {
        cleanWs()
        sh "podman pod rm staging-pod -f"
    }
    success {
        echo "Build success"
    }
    failure {
        echo "Build failed"
    }
  }
}
