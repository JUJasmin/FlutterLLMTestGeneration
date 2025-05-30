import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:automatic_app_test/validated_form.dart';
void main() {
  testWidgets('LoginFormValidation Test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(MaterialApp(home: Scaffold(body: LoginFormValidation())));

    // Verify the submit button is initially disabled.
    expect(tester.widget<ElevatedButton>(find.byKey(Key('submit'))).enabled, false);

    // Test invalid email
    await tester.enterText(find.byKey(Key('username')), 'invalidEmail');
    await tester.pump();

    // Verify the submit button is still disabled.
    expect(tester.widget<ElevatedButton>(find.byKey(Key('submit'))).enabled, false);

    // Test valid email
    await tester.enterText(find.byKey(Key('username')), 'valid@email.com');
    await tester.pump();

    // Verify the submit button is enabled.
    expect(tester.widget<ElevatedButton>(find.byKey(Key('submit'))).enabled, true);
  });
}