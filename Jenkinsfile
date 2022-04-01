pipeline {
  agent { label "sweetheart" }
  environment {
    MYHOME = "$HOME/Documents/django-whatsapp-web-clone"
  }
  stages {
    stage("Build") {
      steps {      
        sh """
            git clone https://github.com/codingelle/django-whatsapp-web-clone.git
            podman pod create -n ci-pod -p 8081:80 -p 8082:8082 -p 6379:6379 -p 5432:5432
            podman run --pod=ci-pod -d --name redis-svc registry.redhat.io/rhel8/redis-5:1-160.1647451816
            podman run --pod=ci-pod -d --name postgres-svc --env-file=$MYHOME/.env registry.redhat.io/rhel8/postgresql-12:1-99.1647451835
        """
        //podman run --pod=ci-pod -d --name app-svc --env-file=$MYHOME/.env localhost/django-app:latest
      }
    }

    stage("Test") {
      steps {
        sh 'podman run -u root --pod ci-pod --name app-svc --env-file=$MYHOME/.env -v $MYHOME/:/opt/app-root/src/ registry.access.redhat.com/ubi8/python-38 bash -c "pip install -U pip && pip install -r requirements.txt && python manage.py migrate && python manage.py createsuperuser --no-input && python manage.py test"'
        //sh 'podman run -u root --pod ci-pod --name app-svc --env-file=$MYHOME/.env -v $MYHOME/:/opt/app-root/src/ registry.access.redhat.com/ubi8/python-38 bash -c "pip install -U pip && pip install -r requirements.txt && python manage.py migrate && python manage.py createsuperuser --no-input && daphne -b 0.0.0.0 -p 8080 django_channel_tutorial.asgi:application && python manage.py test"'
      }
    }

    stage("Deploy") {
      steps {
        echo "Deploy here"
      }
    }
  }
  post {
    // Clean after build
    always {
        cleanWs()
        sh "podman pod rm ci-pod -f"
    }
    success {
        echo "Build success"
    }
    failure {
        echo "Build failed"
    }
  }
}
